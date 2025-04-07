from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from accounts.models import Account
from accounts.serializers import AccountSerializer
import pdb


# Create your views here.
class AccountRegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = Account.objects.create(**serializer.validated_data)
        return Response(model_to_dict(account), status.HTTP_201_CREATED)

    def get(self, request):
        accounts = Account.objects.all()
        accounts_list = []

        for account in accounts:
            account_dict = model_to_dict(account)
            account_dict["courses"] = [
                model_to_dict(course) for course in account.courses.all()
            ]
            accounts_list.append(account_dict)

        return Response(
            {"data": accounts_list, "message": "List of authors listed successfully"},
            status.HTTP_200_OK,
        )


# class AccountLoginView(APIView):
#     def post(self, request):
#         try:
#             account = Account.objects.get(
#                 email=request.data["email"], password=request.data["password"]
#             )
#         except Account.DoesNotExist:
#             return Response({"error": "Account not found"}, status.HTTP_404_NOT_FOUND)

#         return Response(account, status.HTTP_200_OK)
