from django.contrib import admin

# Register your models here.

from .models import About, Experience, Projects, Degrees, Skills

admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(Degrees)
admin.site.register(Skills)