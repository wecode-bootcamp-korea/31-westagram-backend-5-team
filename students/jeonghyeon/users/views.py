import json, re

from django.http  import JsonResponse
from django.views import View

from users.models      import User
from users.vaildation  import vaildation_email, vaildation_password

class SignUpView(View):
    def post(self, request):
        data           = json.loads(request.body)     
        try:  
            email      = data['email']
            name       = data['name']
            phone      = data['phone']
            password   = data['password']
           
            vaildation_email(email)

            vaildation_password(password)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': "User already exists"}, status=401)

            User.objects.create(
                    name     = name,
                    email    = email,
                    phone    = phone,
                    password = password
                )
            return JsonResponse ({"message": "SUCCESS"}, status = 201)
                
        except KeyError:
                return JsonResponse({"message" : "Check Your Data"}, status = 401)
        
class SignInView(View):
        def post(self, request):
            data         = json.loads(request.body)
            try:
                email    = data['email']
                password = data['password']

                if User.objects.filter(email=email, password=password).exists():
                    return JsonResponse({"message": "SUCCESS" }, status = 200)

                else:
                    return JsonResponse( {"message": "INVALID_USER"}, status=401)

            except KeyError:
                return JsonResponse( {"message": "KEYERROR"}, status=400)
