from django.urls import path, include

from users.views import UserSignUpView

urlpatterns = [
    path('/signup',UserSignUpView.as_view()),
]
