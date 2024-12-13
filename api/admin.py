from django.contrib import admin
from .models import CustomUser, CourseDetailsModels, StudentDetailsModels
admin.site.register(CustomUser)
admin.site.register(CourseDetailsModels)
admin.site.register(StudentDetailsModels)

# Register your models here.