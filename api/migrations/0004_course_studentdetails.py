# Generated by Django 5.1.4 on 2024-12-12 09:26

import django.contrib.postgres.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_customuser_role_alter_customuser_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_Ref', models.UUIDField(default=uuid.UUID('f5b5aa77-38ba-44d0-a93f-8a7ca58cc3de'), unique=True)),
                ('course_Id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('course_Name', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(blank=True, choices=[('BASICS', 'basic'), ('ADVANCED', 'advanced'), ('PLACEMENT', 'placement')], null=True)),
                ('duration', models.IntegerField(blank=True)),
                ('fees', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('tools_Technologies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=list, max_length=100), size=None)),
                ('concept', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=list, max_length=100), size=None)),
                ('includes_Internship', models.BooleanField(blank=True, default=False)),
                ('includes_Placement', models.BooleanField(blank=True, default=False)),
                ('shift_Available', models.CharField(blank=True, choices=[('morning', 'Morning '), ('afternoon', 'Afternoon '), ('weekend', 'weekend')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('student_Ref', models.UUIDField(default=uuid.UUID('cdd7ddf7-2bfe-43ab-bf80-257fe713600d'), unique=True)),
                ('student_Id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('student_Fullname', models.CharField(blank=True, max_length=100)),
                ('student_Email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('student_Mobile', models.BigIntegerField(blank=True, null=True)),
                ('student_Age', models.IntegerField(blank=True)),
                ('student_Occupation', models.CharField(choices=[('student', 'student'), ('working professional', 'working professional'), ('freelancer', 'freelancer'), ('other', 'other')])),
                ('student_Other', models.CharField(blank=True, null=True)),
                ('student_intrest', models.CharField(blank=True, null=True)),
                ('student_Ai_Ml', models.BooleanField(blank=True, default=False, null=True)),
                ('student_Experience', models.TextField(blank=True, null=True)),
                ('student_Learn', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=list, max_length=100, null=True), size=None)),
                ('student_Timming', models.CharField(blank=True, choices=[('morning', 'Morning (9:00 AM - 12:30 PM)'), ('afternoon', 'Afternoon (1:30 PM - 5:30 PM)'), ('full_day', 'Full Day (9:00 AM - 5:30 PM)')], max_length=50, null=True)),
                ('student_Payment', models.CharField(blank=True, null=True)),
            ],
        ),
    ]