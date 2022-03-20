import re
from django.forms import ValidationError


REGEX_PASSWORD ='^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


def Vaildation_email(email):
    if not re.match(REGEX_EMAIL, email):
        raise ValidationError('Check_email')

def Vaildation_password(password):
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError('Check_password')