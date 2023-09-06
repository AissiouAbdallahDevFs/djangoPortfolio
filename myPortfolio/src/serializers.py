from rest_framework import serializers
from .models import About, Experience, Projects, Degrees

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class DegreesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degrees
        fields = '__all__'
