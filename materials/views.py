from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateAPIViewSet(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListAPIViewSet(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonRetrieveAPIViewSet(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIViewSet(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonDestroyAPIViewSet(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
