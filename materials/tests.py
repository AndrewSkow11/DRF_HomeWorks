from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from materials.models import Course, Lesson, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("1234")
        self.user.save()

        self.course = Course.objects.create(
            name="Course for testing",
            description="Smth about course",
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name="Lesson for testing",
            description="Smth about lesson 1",
            owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    # def test_list_lessons(self):
    #     response = self.client.get(
    #         reverse('lessons_list')
    #     )
    #
    #     self.assertEquals(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #
    #
    #     data = {
    #         'count': 1,
    #         'next': None,
    #         'previous': None,
    #         'results': [{
    #             'id': 1,
    #             'name': 'Lesson for testing',
    #             'description': 'Smth about lesson 1',
    #             'preview': None,
    #             'course': None,
    #             'owner': 1}]}
    #
    #     # print('json-ответ')
    #     # print(response.json())
    #
    #     self.assertEquals(
    #         response.json(),
    #         data
    #     )
    #


    def test_create_lesson(self):

        data = {
            'name': 'lesson_test_created',
            'description': 'test description 2',
            'course': 1,
            # 'viedo': 'youtube.com/watch/1234'
        }

        response = self.client.post(
            reverse('lesson_create'),
            data
        )
        print(response)
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )