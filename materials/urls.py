from django.urls import path
from materials.views import (
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonCreateAPIView,
    CourseAPIViewSet,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register("course", CourseAPIViewSet)

urlpatterns = [
                  path("lessons/", LessonListAPIView.as_view(),
                       name="lesson_list"),
                  path("lesson/create/", LessonCreateAPIView.as_view(),
                       name="lesson_create"),
                  path("lesson/update/<int:pk>/",
                       LessonUpdateAPIView.as_view(), name="lesson_update"),
                  path("lesson/detail/<int:pk>/",
                       LessonRetrieveAPIView.as_view(),
                       name="lesson_delete"),
                  path(
                      "lesson/delete/<int:pk>/",
                      LessonDestroyAPIView.as_view(),
                      name="lesson_destroy"),
              ] + router.urls
