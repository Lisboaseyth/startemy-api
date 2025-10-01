from django.urls import path
from accounts.views import AccountRegisterView, AccountProfileView, TokenVerifyAndRefreshView

urlpatterns = [
    path("register/", AccountRegisterView.as_view()),
    path("profile/", AccountProfileView.as_view(), name="profile"),
    path("token/verify-refresh/", TokenVerifyAndRefreshView.as_view(), name="token_verify_refresh"),
]
