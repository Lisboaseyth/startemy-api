from django.urls import path
from accounts.views import AccountRegisterView, AccountProfileView

urlpatterns = [
    path("register/", AccountRegisterView.as_view()),
    path("profile/", AccountProfileView.as_view(), name="profile"),
]
