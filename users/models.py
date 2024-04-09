from django.db import models
# 1. Пользователь:
# - все поля от обычного пользователя, но авторизацию заменить на email;
# - телефон;
# - город;
# - аватарка.

from django.contrib.auth.models import AbstractUser

NULLABLE = {
    "blank": True,
    "null": True,
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="email")

    avatar = models.ImageField(upload_to="users/",
                               verbose_name="аватар", **NULLABLE)
    phone_number = models.CharField(
        max_length=35, verbose_name="номер телефона", **NULLABLE)
    city = models.CharField(max_length=255, verbose_name="город",
                               **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []