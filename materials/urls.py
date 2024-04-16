from django.urls import path
from materials.views import (
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonCreateAPIView,
    CourseAPIViewSet)
from rest_framework import routers

router = routers.SimpleRouter()
router.register("course", CourseAPIViewSet)

urlpatterns = [
                  path("lessons/",
                       LessonListAPIView.as_view(),
                       name="lesson_list"),
                  path("lesson/create/",
                       LessonCreateAPIView.as_view(),
                       name="lesson_create"),
                  path("lesson/<int:pk>/update/",
                       LessonUpdateAPIView.as_view(),
                       name="lesson_update"),
                  path("lesson/<int:pk>/detail/",
                       LessonRetrieveAPIView.as_view(),
                       name="lesson_detail"),
                  path(
                      "lesson/<int:pk>/delete/",
                      LessonDestroyAPIView.as_view(),
                      name="lesson_destroy"),

              ] + router.urls
