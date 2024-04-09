from django.urls import path
from materials.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('course', CourseAPIViewSet)

urlpatterns = [
                  path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson_create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson_detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_delete'),
                  path('lesson_delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
] + router.urls
