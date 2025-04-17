from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from accounts.models import User
from accounts.serializers import AccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AccountRegisterView(APIView):

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(AccountSerializer(user).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        accounts = User.objects.all()
        serializer = AccountSerializer(accounts, many=True)

        return Response(
            {"data": serializer.data, "message": "List of authors listed successfully"},
            status=status.HTTP_200_OK,
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        token["id"] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
        }
        return {
            "data": data,
            "message": "Usuário logado com sucesso!"
        }


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
