from django.core.management import BaseCommand
import datetime
from materials.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **kwargs):
        Payment.objects.all().delete()

        user1, created = User.objects.get_or_create(email='user1@test.ru')
        user2, created = User.objects.get_or_create(email='user2@test.ru')

        course1, created = Course.objects.get_or_create(name='Курс 1')
        course2, created = Course.objects.get_or_create(name='Курс 2')

        lesson1, created = Lesson.objects.get_or_create(name='Урок 1')
        lesson2, created = Lesson.objects.get_or_create(name='Урок 2')

        Payment.objects.create(
            user=user1,
            date=datetime.datetime.now().date,
            amount=500,
            payment_type='cash',
            course=course1)

        Payment.objects.create(
            user=user2,
            date=datetime.datetime.now().date,
            amount=5000,
            payment_type='spending',
            course=course2)

        Payment.objects.create(
            user=user2,
            date=datetime.datetime.now().date,
            amount=150,
            payment_type='spending',
            lesson=lesson1, )

        Payment.objects.create(
            user=user1,
            date=datetime.datetime.now().date,
            amount=150,
            payment_type='cash',
            lesson=lesson1, )

        self.stdout.write(self.style.SUCCESS("Данные для тестирования"
                                             " системы загружены"))
