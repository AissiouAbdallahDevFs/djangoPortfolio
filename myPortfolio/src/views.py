from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

class IsSuperuserAndAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class UserViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()  
    serializer_class = UserSerializer  

class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    skills = Skills.objects.all()
    serializer_class = AboutSerializer
    
    @action(detail=False, methods=['get'])
    def get_action(self, request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def add_action(self, request):
        if request.user.is_authenticated:
            message = {'detail': 'Added Successfully'}
            serializer = AboutSerializer(data=request.data)
            skills = Skills.objects.all()
            if serializer.is_valid():
                serializer.save()
                return Response( message,status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        if request.user.is_authenticated:
            message = {'detail': 'Delete Successfully'}
            about = About.objects.get(id=id)
            about.delete()
            if about:
                return Response(status=status.HTTP_200_OK,message=message)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        if request.user.is_authenticated:
            about = About.objects.get(id=id)
            about.save()
            if about:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)



class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    @action(detail=False, methods=['get'])
    def get_action(self, request):
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def add_action(self, request):
        if request.user.is_authenticated:
            message = {'detail': 'Added Successfully'}
            serializer = ExperienceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(message, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['delete'])
    def delete_action(self, request, id):
        if request.user.is_authenticated:
            message = {'detail': 'Delete Successfully'}
            id = self.kwargs.get('id')
            try:
                experience = Experience.objects.get(id=id)
                experience.delete()
                return Response(message, status=status.HTTP_200_OK)
            except Experience.DoesNotExist:
                return Response({'detail': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['put'])
    def put_action(self, request):
        if request.user.is_authenticated:
            experiences = Experience.objects.all()
            serializer = ExperienceSerializer(experiences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

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
         if request.user.is_authenticated:
            message = {'detail': 'Added Successfully'}
            serializer = ProjectsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( message,status=status.HTTP_201_CREATED)
            return Response( status=status.HTTP_400_BAD_REQUEST)
         else:
                return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
       
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        if request.user.is_authenticated:
            message = {'detail': 'Delete Successfully'}
            id = self.kwargs.get('id')
            print(id)
            projects = Projects.objects.get(id=id)
            projects.delete()
            if projects:
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        if request.user.is_authenticated:
            projects = Projects.objects.get(id=id)
            projects.save()
            if projects:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    

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
        if request.user.is_authenticated:
            message = {'detail': 'Added Successfully'}
            serializer = DegreesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( message,status=status.HTTP_201_CREATED)
            return Response( status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        if request.user.is_authenticated:
            message = {'detail': 'Delete Successfully'}
            degrees = Degrees.objects.get(id=id)
            degrees.delete()
            if degrees:
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        if request.user.is_authenticated:
            degrees = Degrees.objects.get(id=id)
            degrees.save()
            if degrees:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

    @action(detail=False, methods=['get'])
    def get_action(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response( status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def add_action(self, request):
        if request.user.is_authenticated:
            message = {'detail': 'Added Successfully'}
            serializer = SkillsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( message,status=status.HTTP_201_CREATED)
            return Response( status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['delete'])
    def delete_action(self, request,id):
        if request.user.is_authenticated:
            message = {'detail': 'Delete Successfully'}
            skills = Skills.objects.get(id=id)
            skills.delete()
            if skills:
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['put'])
    def put_action(self, request,id):
        if request.user.is_authenticated:
            skills = Skills.objects.get(id=id)
            skills.save()
            if skills:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
