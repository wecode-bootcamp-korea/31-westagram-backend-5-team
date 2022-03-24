import json, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View
from django.conf  import settings

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
                    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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

                user = User.objects.get(email=email)

                if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    return JsonResponse( {'message': 'INVALID_USER'}, status=401)

                token = jwt.encode({'user_id':user.id}, settings.SECRET_KEY, settings.ALGORITHM)

                return JsonResponse({'message': 'SUCCESS','Authorization':token} ,status = 200)

            except User.DoesNotExist:
                return JsonResponse( {'message': 'YOUR EMAIL DOES NOT EXIST'}, status=400)

            except KeyError:
                return JsonResponse( {'message': 'KEY_ERROR'}, status=400)
                