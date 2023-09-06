from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = UserSerializer  

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    
    @action(detail=False, methods=['get'])
    def get_action(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def add_action(self, request):
        message = {'detail': 'Added Successfully'}
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( message,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        message = {'detail': 'Delete Successfully'}
        about = About.objects.get(id=id)
        about.delete()
        if about:
            return Response(status=status.HTTP_200_OK,message=message)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        about = About.objects.get(id=id)
        about.save()
        if about:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ExperienceViewSet(viewsets.ModelViewSet):
    
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
   

    @action(detail=False, methods=['get'])
    def get_action(self, request):
        
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response( status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def add_action(self, request):
        message = {'detail': 'Added Successfully'}
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( message,status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        message = {'detail': 'Delete Successfully'}
        id = self.kwargs.get('id')
        print(id)
        experiences = Experience.objects.get(id=id)
        experiences.delete()
        if experiences:
            return Response(message, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def put_action(self, request):
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(status=status.HTTP_200_OK)

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    @action(detail=False, methods=['get'])
    def get_action(self, request):
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response( status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def add_action(self, request):
        message = {'detail': 'Added Successfully'}
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( message,status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        message = {'detail': 'Delete Successfully'}
        id = self.kwargs.get('id')
        print(id)
        projects = Projects.objects.get(id=id)
        projects.delete()
        if projects:
            return Response(message, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        projects = Projects.objects.get(id=id)
        projects.save()
        if projects:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class DegreesViewSet(viewsets.ModelViewSet):
    queryset = Degrees.objects.all()
    serializer_class = DegreesSerializer

    @action(detail=False, methods=['get'])
    def get_action(self, request):
        degrees = Degrees.objects.all()
        serializer = DegreesSerializer(degrees, many=True)
        return Response( status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def add_action(self, request):
        message = {'detail': 'Added Successfully'}
        serializer = DegreesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( message,status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        message = {'detail': 'Delete Successfully'}
        degrees = Degrees.objects.get(id=id)
        degrees.delete()
        if degrees:
            return Response(message, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        degrees = Degrees.objects.get(id=id)
        degrees.save()
        if degrees:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
