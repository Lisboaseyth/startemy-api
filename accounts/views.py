from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from accounts.models import Account


# Create your views here.
class AccountRegisterView(APIView):
    def post(self, request):
        account = account.objects.create(**request.data)
        account_dict = model_to_dict(account)

        return Response(account_dict, status.HTTP_201_CREATED)


class AccountLoginView(APIView):
    def post(self, request):
        try:
            account = Account.objects.get(
                email=request.data["email"], password=request.data["password"]
            )
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status.HTTP_404_NOT_FOUND)

        return Response(account, status.HTTP_200_OK)
