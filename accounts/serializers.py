from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "document",
            "phone",
            "birthdate",
            "study_level",
            "gender",
            "created_at",
            "updated_at",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
