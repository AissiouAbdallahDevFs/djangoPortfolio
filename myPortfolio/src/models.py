from django.db import models
from django.db import models
from django.contrib.auth.models import User  # Importez la classe User de Django

class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associez l'utilisateur à l'objet
    aboutName = models.CharField(max_length=200)
    aboutDescription = models.TextField()
    aboutImage = models.ImageField(upload_to='images/')
    skills = models.ManyToManyField('Skills')

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associez l'utilisateur à l'objet
    experienceName = models.CharField(max_length=200)
    experienceDescription = models.TextField()
    experienceImage = models.ImageField(upload_to='images/')
    experienceDate = models.DateTimeField(auto_now_add=True)

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associez l'utilisateur à l'objet
    projectsName = models.CharField(max_length=200)
    projectsDescription = models.TextField()
    projectsImage = models.ImageField(upload_to='images/')
    projectsDate = models.DateTimeField(auto_now_add=True)

class Degrees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associez l'utilisateur à l'objet
    degreesName = models.CharField(max_length=200)
    degreesDescription = models.TextField()
    degreesImage = models.ImageField(upload_to='images/')
    degreesDate = models.DateTimeField(auto_now_add=True)

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associez l'utilisateur à l'objet
    skillsName = models.CharField(max_length=200)
    skillsDescription = models.TextField()
    skillsImage = models.ImageField(upload_to='images/')
    skillsDate = models.DateTimeField(auto_now_add=True)

