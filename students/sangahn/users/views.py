import json

from django.http import JsonResponse
from django.views import View
from django.db import IntegrityError
from django.core.exceptions import ValidationError 

from users.models import User
from users.validator import validate_email, validate_password

class SignUpView(View):
    def post(self,request):
        try:
            data         = json.loads(request.body)
            name         = data['name']
            email        = data['email']
            password     = data['password']
            phone_number = data['phone_number']

            validate_email(email)
            validate_password(password)

            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number
            )
            return JsonResponse({"message":"SUCCESS"}, status=201) 
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"},status=400)
        except IntegrityError:
            return JsonResponse({'message':'EMAIL_OVERLAP_ERROR'},status=400)
        except ValidationError as error:
            return JsonResponse({'message' : error.message},status=400)