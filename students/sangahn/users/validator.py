import re

from django.core.exceptions import ValidationError 

EMAIL_FORMAT    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_FORMAT = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

def validate_email(email):
    if not re.match(EMAIL_FORMAT, email):
        raise  ValidationError("EMAIL_FORMAT_ERROR")

def validate_password(password):
    if not re.match(PASSWORD_FORMAT, password):
        raise ValidationError("PASSWORD_FORMAT_ERROR")

def overlap_email(email):
    if User.objects.filter(email=email).exists():
        raise ValidationError("EMAIL_OVERLAP_ERROR")

def validate_sign_up(email,password):
    if not User.objects.filter(email=email,password=password).exists():
        raise ValidationError("INVALID_USER")