from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class AboutSerializer(serializers.ModelSerializer):
    skills = Skills.objects.all()
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

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
