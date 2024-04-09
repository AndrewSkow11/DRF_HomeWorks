from django.urls import path
from materials.views import *


urlpatterns = [
    path('', LessonListAPIView.as_view(), name='lesson_list'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_delete'),
    path('delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
]