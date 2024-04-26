from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="email")
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="аватар",
        blank=True,
        null=True)
    phone_number = models.CharField(
        max_length=35,
        verbose_name="номер телефона",
        blank=True,
        null=True)
    city = models.CharField(
        max_length=255,
        verbose_name="город",
        blank=True,
        null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


# 1) Логика должна быть описана для уже существующей модели Payment, новую модель создавать не нужно
# 2) Сервисы для работы с Stripe у тебя описаны, осталось лишь встроить их в логику системы. При создании платежа необходимо вызвать эти сервисы. Полученный id сессии и ссылку для оплаты нужно отдать пользователю в ответ на создание платежа и сохранить эти данные в созданный объект платежа. Для этого нужно добавить два новых поля в Payment - session_id и payment_link


class Payment(models.Model):
    class PaymentType(models.TextChoices):
        CASH = 'cash', 'наличные'
        SPENDING = 'spending', 'перевод на счет'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name='payment',
        verbose_name='пользователь',
        null=True, blank=True)
    date = models.DateField(
        auto_now=True,
        verbose_name='дата оплаты')
    course = models.ForeignKey(
        'materials.Course',
        on_delete=models.SET_NULL,
        verbose_name='оплаченный курс',
        null=True,
        blank=True)
    lesson = models.ForeignKey(
        'materials.Lesson',
        on_delete=models.SET_NULL,
        verbose_name='оплаченный урок',
        null=True,
        blank=True)
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='сумма оплаты')
    payment_type = models.CharField(
        max_length=32,
        choices=PaymentType.choices,
        verbose_name='способ оплаты')

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('user', 'date')
