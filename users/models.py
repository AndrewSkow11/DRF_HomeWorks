from django.db import models
# 1. Пользователь:
# - все поля от обычного пользователя, но авторизацию заменить на email;
# - телефон;
# - город;
# - аватарка.

from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson

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


class Payment(models.Model):
    class PaymentType(models.TextChoices):
        CASH = 'cash', 'наличные'
        SPENDING = 'spending', 'перевод на счет'

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             related_name='payment',
                             verbose_name='пользователь',
                             null=True, blank=True)
    date = models.DateField(auto_now=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,
                               verbose_name='оплаченный курс', null=True,
                               blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL,
                               verbose_name='оплаченный урок',
                               null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2,
                                 verbose_name='сумма оплаты')
    payment_type = models.CharField(max_length=32, choices=PaymentType.choices,
                                    verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('user', 'date')


