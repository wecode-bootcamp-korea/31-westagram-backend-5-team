import json

from django.http import JsonResponse
from django.views import View
from django.db import IntegrityError

from users.models import User
from users.validator import validate_email, validate_password

class UserSignUpView(View):
    def post(self,request):
        try:
            data               = json.loads(request.body)
            input_name         = data['name']
            input_email        = data['email']
            input_password     = data['password']
            input_phone_number = data['phone_number']

            email_validation    = validate_email(input_email)
            password_validation = validate_password(input_password)

            if not email_validation:
                return JsonResponse({'message':'EMAIL_FORMAT_ERROR'},status=400)
            if not password_validation:
                return JsonResponse({'message':'PASSWORD_FORMAT_ERROR'},status=400)

            User.objects.create(
                name         = input_name,
                email        = input_email,
                password     = input_password,
                phone_number = input_phone_number
            )
            return JsonResponse({"message":"SUCCESS"}, status=201) 
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)
        except IntegrityError:
            return JsonResponse({'message':'EMAIL_OVERLAP_ERROR'},status=400)