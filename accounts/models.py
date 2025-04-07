from django.db import models


class GenderAccount(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    NOT_INFORMED = "Not Informed"


class Account(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    document = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    birthdate = models.DateField()
    study_level = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=20, choices=GenderAccount.choices, default=GenderAccount.NOT_INFORMED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
