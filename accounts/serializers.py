from rest_framework import serializers
from accounts.models import GenderAccount

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField()
    document = serializers.CharField(max_length=15)
    phone = serializers.CharField(max_length=15)
    birthdate = serializers.DateField()
    study_level = serializers.CharField(max_length=50)
    gender = serializers.ChoiceField(choices=GenderAccount.choices)