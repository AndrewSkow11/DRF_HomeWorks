from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_url_resource


class LessonSerializer(serializers.ModelSerializer):

    video = serializers.CharField(validators=validate_url_resource)

    class Meta:
        model = Lesson
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        lesson = Lesson(**validated_data)
        lesson.owner = user
        lesson.save()
        return lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, instance):
        return instance.lesson.count()

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        course = Course(**validated_data)
        course.owner = user
        course.save()
        return course
