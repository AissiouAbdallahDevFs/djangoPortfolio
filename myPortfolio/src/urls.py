from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from views import *

router = DefaultRouter()
router.register(r'experience', views.ExperienceViewSet)

urlpatterns = [
    # url de la views ExperienceViewSet
    path('experience/', ExperienceViewSet.as_view({'get': 'custom_action'}), name='custom-experience'),
    path('experience/add', ExperienceViewSet.as_view({'post': 'custom_action'}), name='Experience'),
    path('experience/delete', ExperienceViewSet.as_view({'delete': 'custom_action'}), name='Experience'),
    path('experience/update', ExperienceViewSet.as_view({'put': 'custom_action'}), name='Experience'),
    # url de la views AboutViewSet
    path('about/custom/', AboutViewSet.as_view({'get': 'custom_action'}), name='custom-about'),
    path('about/add', AboutViewSet.as_view({'post': 'custom_action'}), name='About'),
    path('about/delete', AboutViewSet.as_view({'delete': 'custom_action'}), name='About'),
    path('about/update', AboutViewSet.as_view({'put': 'custom_action'}), name='About'),
    # url de la views ProjectsViewSet
    path('projects/', ProjectsViewSet.as_view({'get': 'custom_action'}), name='custom-projects'),
    path('projects/add', ProjectsViewSet.as_view({'post': 'custom_action'}), name='Projects'),
    path('projects/delete', ProjectsViewSet.as_view({'delete': 'custom_action'}), name='Projects'),
    path('projects/update', ProjectsViewSet.as_view({'put': 'custom_action'}), name='Projects'),
    # url de la views DegreesViewSet
    path('degrees/', DegreesViewSet.as_view({'get': 'custom_action'}), name='custom-degrees'),
    path('degrees/add', DegreesViewSet.as_view({'post': 'custom_action'}), name='Degrees'),
    path('degrees/delete', DegreesViewSet.as_view({'delete': 'custom_action'}), name='Degrees'),
    path('degrees/update', DegreesViewSet.as_view({'put': 'custom_action'}), name='Degrees'),
     
]