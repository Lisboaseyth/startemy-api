from django.urls import path
from accounts.views import AccountRegisterView

urlpatterns = [
    path("register/", AccountRegisterView.as_view()),
]
