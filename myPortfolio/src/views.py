from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import About, Experience, Projects, Degrees
from .serializers import AboutSerializer, ExperienceSerializer, ProjectsSerializer, DegreesSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    @action(detail=False, methods=['get', 'post', 'put', 'patch', 'delete'])
    def custom_action(self, request):
        # Votre logique personnalisée ici
        data = {'message': 'Action personnalisée réussie !'}
        return Response(data, status=200)

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class DegreesViewSet(viewsets.ModelViewSet):
    queryset = Degrees.objects.all()
    serializer_class = DegreesSerializer
