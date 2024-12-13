# Generated by Django 5.1.4 on 2024-12-12 09:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_course_course_id_alter_course_course_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_Id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_Ref',
            field=models.UUIDField(default=uuid.UUID('f65309e3-3d43-40b4-a71d-9def3f7e5da3'), unique=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='student_Id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='student_Ref',
            field=models.UUIDField(default=uuid.UUID('5e42746c-3090-4be1-abd6-2365fa61c6af'), unique=True),
        ),
    ]