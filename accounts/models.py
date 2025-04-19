from django.db import models
from django.contrib.auth.models import AbstractUser


class GenderAccount(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    NOT_INFORMED = "Not Informed"


class User(AbstractUser):
    document = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    birthdate = models.DateField()
    study_level = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=20, choices=GenderAccount.choices, default=GenderAccount.NOT_INFORMED
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
