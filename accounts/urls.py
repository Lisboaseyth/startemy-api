from django.urls import path
from accounts.views import AccountRegisterView
from rest_framework_simplejwt import views

urlpatterns = [
    path("register/", AccountRegisterView.as_view()),
    path("token/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
]