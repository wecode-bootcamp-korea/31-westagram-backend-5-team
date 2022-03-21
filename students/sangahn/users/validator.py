import re

from django.core.exceptions import ValidationError 

def validate_email(email):
    EMAIL_FORMAT = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if not re.match(EMAIL_FORMAT, email):
        raise  ValidationError("EMAIL_FORMAT_ERROR")
def validate_password(password):
    PASSWORD_FORMAT = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

    if not re.match(PASSWORD_FORMAT, password):
        raise ValidationError("PASSWORD_FORMAT_ERROR")