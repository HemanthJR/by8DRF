# Generated by Django 5.1.4 on 2024-12-12 06:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('tutor', 'Tutor'), ('admin', 'Admin')], default='student', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=225)),
                ('occupation', models.CharField(choices=[('student', 'student'), ('working_professional', 'working professional'), ('freelancer', 'freelancer'), ('others', 'others')], max_length=50)),
                ('institute_name', models.CharField(blank=True, max_length=255, null=True)),
                ('interest', models.CharField(blank=True, max_length=255, null=True)),
                ('worked_in_ai_ml', models.BooleanField()),
                ('ai_experience_details', models.TextField(blank=True, null=True)),
                ('excited_to_learn', models.JSONField(default=list)),
                ('session_timing', models.CharField(blank=True, choices=[('morning', 'Morning (9:00 AM - 12:30 PM)'), ('afternoon', 'Afternoon (1:30 PM - 5:30 PM)'), ('full_day', 'Full Day (9:00 AM - 5:30 PM)')], max_length=50, null=True)),
                ('payment_proof', models.CharField(max_length=5000)),
                ('agreement', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]