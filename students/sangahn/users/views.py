import json, bcrypt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError 

from users.models    import User
from users.validator import *

class SignUpView(View):
    def post(self,request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            validate_email(email)
            check_email_duplication(email)
            validate_password(password)

            password_encrypt = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            
            User.objects.create(
                name         = name,
                email        = email,
                password     = password_encrypt,
                phone_number = phone_number
            )
            return JsonResponse({"message" : "SUCCESS"} , status=201) 
        except KeyError: 
            return JsonResponse({"message" : "KEY_ERROR"} , status=400)
        except ValidationError as error: 
            return JsonResponse({'message' : error.message} , status=400)

class SignInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email,password=password).exists():
                return JsonResponse({"message" : "INVALID_USER"} , status=401)
            
            return JsonResponse({"message" : "SUCCESS"} , status=200)
        except KeyError: 
            return JsonResponse({"message" : "KEY_ERROR"} , status=400)