from datetime import timezone

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView, get_object_or_404,
)
from rest_framework.views import APIView
from materials.models import Course, Lesson, CourseSubscription
from materials.paginations import LessonCoursePaginator
from materials.permissions import IsModerator, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.tasks import send_info_about_update_course

class CourseAPIViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    pagination_class = LessonCoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner, ~IsModerator]
        return [permission() for permission in self.permission_classes]

    def perform_update(self, serializer):
        course = serializer.save()
        course_id = course.id

        # sending mail with celery
        send_info_about_update_course.delay(course_id)

        # sending mail without celery
        # send_info_about_update_course(course_id)


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [
        IsAuthenticated, ~IsModerator
    ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    pagination_class = LessonCoursePaginator

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderator').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class SubscribtionCourseAPIView(APIView):
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item, created = CourseSubscription.objects.get_or_create(
            user=user,
            course=course_item)

        if created:
            message = 'подписка добавлена'
        else:
            subs_item.delete()
            message = 'подписка удалена'

        return Response(message)
