from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)


from materials.models import Course
from materials.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonCreateAPIViewSet(CreateAPIView):
    pass

class LessonListAPIViewSet(ListAPIView):
    pass

class LessonRetrieveAPIViewSet(RetrieveAPIView):
    pass

class LessonUpdateAPIViewSet(UpdateAPIView):
    pass

class LessonDestroyAPIViewSet(DestroyAPIView)
    pass