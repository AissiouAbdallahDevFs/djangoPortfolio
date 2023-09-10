from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.register(r'experience', views.ExperienceViewSet)
router.register(r'about', AboutViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'degrees', DegreesViewSet)

urlpatterns = [
    # url de la views ExperienceViewSet
    path('experience/', ExperienceViewSet.as_view({'get': 'get_action'}), name='custom-experience'),
    path('experience/add', ExperienceViewSet.as_view({'post': 'add_action'}), name='Experience'),
    path('experience/delete/<int:id>', ExperienceViewSet.as_view({'delete': 'delete_action'}), name='Experience'),
    path('experience/update/<int:id>', ExperienceViewSet.as_view({'put': 'put_action'}), name='Experience'),
    # url de la views AboutViewSet
    path('about/', AboutViewSet.as_view({'get': 'get_action'}), name='custom-about'),
    path('about/add', AboutViewSet.as_view({'post': 'add_action'}), name='About'),
    path('about/delete/<int:id>', AboutViewSet.as_view({'delete': 'delete_action'}), name='About'),
    path('about/update/<int:id>', AboutViewSet.as_view({'put': 'put_action'}), name='About'),
    # url de la views ProjectsViewSet
    path('projects/', ProjectsViewSet.as_view({'get': 'get_action'}), name='custom-projects'),
    path('projects/add', ProjectsViewSet.as_view({'post': 'add_action'}), name='Projects'),
    path('projects/delete/<int:id>', ProjectsViewSet.as_view({'delete': 'delete_action'}), name='Projects'),
    path('projects/update/<int:id>', ProjectsViewSet.as_view({'put': 'put_action'}), name='Projects'),
    # url de la views DegreesViewSet
    path('degrees/', DegreesViewSet.as_view({'get': 'get_action'}), name='custom-degrees'),
    path('degrees/add', DegreesViewSet.as_view({'post': 'add_action'}), name='Degrees'),
    path('degrees/delete/<int:id>', DegreesViewSet.as_view({'delete': 'delete_action'}), name='Degrees'),
    path('degrees/update/<int:id>', DegreesViewSet.as_view({'put': 'put_action'}), name='Degrees'),
    # url de la views SkillsViewSet
    path('skills/', SkillsViewSet.as_view({'get': 'get_action'}), name='custom-skills'),
    path('skills/add', SkillsViewSet.as_view({'post': 'add_action'}), name='Skills'),
    path('skills/delete/<int:id>', SkillsViewSet.as_view({'delete': 'delete_action'}), name='Skills'),
    path('skills/update/<int:id>', SkillsViewSet.as_view({'put': 'put_action'}), name='Skills'),
    # url de la views MessagesViewSet
    path('messages/', MessagesViewSet.as_view({'get': 'get_action'}), name='custom-messages'),
    path('messages/add', MessagesViewSet.as_view({'post': 'add_action'}), name='Messages'),
    path('messages/delete/<int:id>', MessagesViewSet.as_view({'delete': 'delete_action'}), name='Messages'),
    path('messages/update/<int:id>', MessagesViewSet.as_view({'put': 'put_action'}), name='Messages'),
     
]