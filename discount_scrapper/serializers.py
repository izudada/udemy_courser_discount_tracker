from rest_framework import serializers

from discount_scrapper.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"