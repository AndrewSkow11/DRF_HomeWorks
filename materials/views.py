from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseAPIViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
