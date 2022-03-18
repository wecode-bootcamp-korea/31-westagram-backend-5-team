import re

def validate_email(email):
    EMAIL_FORMAT = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    email_validation = re.match(EMAIL_FORMAT, email)
    return email_validation
def validate_password(password):
    PASSWORD_FORMAT = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

    password_validation = re.match(PASSWORD_FORMAT, password)
    return password_validation