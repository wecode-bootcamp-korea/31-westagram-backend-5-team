import json, re

from django.http  import JsonResponse
from django.views import View

from .models import User

Minimum_Password_Number = 8

class SignUpView(View):
    def post(self, request):
        try:
            data       = json.loads(request.body)       
            email      = data['email']
            name       = data['name']
            phone      = data['phone']
            password   = data['password']
           
            if not(email and name and phone and password):
                raise KeyError

            email_pattern = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not email_pattern.match(email):
                return JsonResponse({"message" : "KEYERROR"}, status = 400)

            password_pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
            if not password_pattern.match(password):
                return JsonResponse({"message" : "KEYERROR"}, status = 400)        

            if len(password) < Minimum_Password_Number:
                return JsonResponse({'message':'SHORT_PASSWORD'}, status=400)
        
            users =  User.objects.filter(email=email)
            if not users:
                User.objects.create(
                    name = name,
                    email    = email,
                    phone    = phone,
                    password = password
                )
                return JsonResponse ({"message": "SUCCESS"}, status = 201)
                
            else:
                return JsonResponse({'message': "KEYERROR"}, staus=400)    
        
        except KeyError:
                return JsonResponse({"message" : "KEYERROR"}, status = 400)