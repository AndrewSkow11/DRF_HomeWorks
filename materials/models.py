from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='course_preview',
                                verbose_name='превью', null=True, blank=True)
    description = models.TextField(verbose_name='описание')


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='крус',
                               related_name='course',
                               on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson_preview',
                                verbose_name='превью', null=True, blank=True)
    video = models.FileField(upload_to='video_lesson', blank=True, null=True)
