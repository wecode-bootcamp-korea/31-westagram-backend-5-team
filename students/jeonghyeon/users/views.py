# Create your views here.
import json, re

from django.http  import JsonResponse
from django.views import View

from models import User

Minimum_Password_Number = 7

#유효성 검사부분 
class Validation(View):
    def post (self, request):
        data = json.loads[request.body]

        def vaildate_email(email):
            pattern = re.compile('/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/')
            if not pattern.match(email):
                return JsonResponse({"message" : "KEYERROR"}, status = 400)
        
        def vaildate_password(password):
            pattern = re.compile('/^(?=.?[A-Z])(?=.?[a-z])(?=.?[0-9])(?=.?[#?!@$ %^&*-]).{8,}$/')
            if not pattern.match(pattern):
                return JsonResponse({"message" : "KEYERROR"}, status = 400)

            if password < Minimum_Password_Number:
                return JsonResponse({"message" : "KEYERROR"}, status = 400)

        def vaildate_phone(phone):
            pattern = re.compile('휴대폰번호: /^01(?:0|1|[6-9])[.-]?(\\d{3}|\\d{4})[.-]?(\\d{4})$/')
            if not pattern.match(phone):
                return JsonResponse({"message" : "KEYERROR"}, status = 400)


class SignUpView(View):
    def post(self, request):
        data = json.loads[request.body]
        #받아오자
        try:
            email    = data['email']
            name     = data['name']
            phone    = data['phone']
            password = data['password']
        

            #잘 들어왔나..
            if Not(email and name and phone and password):
                return JsonResponse({"message" : "KEYERROR"}, status = 400)


            #유효성 검사해주ㅡㅁㄴㅇㄹㅁㄴㅇㄹㅁ위에서 정의한거
            Validation.vaildate_email(email)
            Validation.vaildate_password(password)
            Validation.vaildate_phone(phone)

            #중복도 검사해야하네? ㅎㅎㅎㅎㅎ
            users =  User.objects.filter(email=email)
            #중복검사해서 없으면 추가
            if not users:
                User.objects.create(
                    name     = name,
                    email    = email,
                    phone    = phone,
                    password = password
                )
                
                return JsonResponse ({"message": "SUCCESS"}, status = 201)

            return JsonResponse({'message': "user already exist"})    
        
        except KeyError:
            return JsonResponse({"message" : "KEYERROR"}, status = 400)


	