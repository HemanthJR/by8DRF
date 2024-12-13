from django.contrib.auth.models import AbstractUser 
from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField

class CustomUser(AbstractUser): 
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True) 
    mobile = models.CharField(max_length=10, null=True, blank=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self): 
        return self.email
    
class CourseDetailsModels(models.Model):
    course_Ref = models.UUIDField(unique=True,default=uuid.uuid4())
    course_Id = models.CharField(max_length=100,primary_key=True,unique=True)
    course_Name = models.CharField(max_length=100, null=False, blank=True)
    category = models.CharField(choices=[
        ('basic','basic'),
        ('advanced','advanced'),
        ('placement','placement')
    ], null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    fees = models.DecimalField(null=False, max_digits=6, decimal_places=2, blank=True)
    tools_Technologies = ArrayField(models.CharField(max_length=100,blank=True, default=list))
    concept = ArrayField(models.CharField(max_length=100,blank=True, default=list))
    includes_Internship = models.BooleanField(default=False, blank=True)
    includes_Placement = models.BooleanField(default=False, blank=True)
    shift_Available = models.CharField(choices=[
        ('morning', 'Morning '), 
        ('afternoon', 'Afternoon '), 
        ('weekend', 'weekend'), ], null=True, blank=True)
    
    def __str__(self):
        return str(self.course_Id)

class StudentDetailsModels(models.Model):
    student_Ref = models.UUIDField(unique=True,default=uuid.uuid4())
    student_Id = models.AutoField(primary_key=True,unique=True)
    student_Fullname = models.CharField(max_length=100, null=False, blank=False)
    student_Email = models.EmailField(unique=True, null=False, blank=False)
    student_Mobile = models.BigIntegerField(null=False, blank=False)
    student_Dob = models.CharField(max_length=50, null=True, blank=True)   
    student_Location = models.CharField(max_length=50, null=False, blank=False)
    student_Occupation = models.CharField(choices=[
        ('student','student'),
        ('working professional', 'working professional'),
        ('freelancer', 'freelancer'),
        ('other', 'other')
    ], null=False, blank=False)
    student_Other = models.CharField(null=True)
    student_intrest = models.CharField(null=True, blank=True)
    student_Organization = models.CharField(max_length=200,null=True, blank=True)
    student_Ai_Ml = models.BooleanField(null=False, default=False, blank=False)
    student_Experience = models.TextField(null=True, blank=True)
    student_Learn = ArrayField(models.CharField(max_length=100,blank=True,null=True,default=list))
    student_Timming = models.CharField(max_length=50, choices=[ 
        ('morning', 'Morning (9:00 AM - 12:30 PM)'), 
        ('afternoon', 'Afternoon (1:30 PM - 5:30 PM)'), 
        ('full_day', 'Full Day (9:00 AM - 5:30 PM)'), ], null=True, blank=True)
    student_Payment = models.CharField(null=False, blank=False)

    def __str__(self):
        return str(self.student_Id)


    
    
    