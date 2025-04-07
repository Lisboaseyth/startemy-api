from django.urls import path
from accounts.views import AccountRegisterView, AccountLoginView

urlPatterns = [
    path("register/", AccountRegisterView.as_view()),
    path("login/", AccountLoginView.as_view()),
]