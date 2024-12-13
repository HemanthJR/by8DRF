# Generated by Django 5.1.4 on 2024-12-12 09:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_course_course_ref_alter_course_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_Ref',
            field=models.UUIDField(default=uuid.UUID('13515eb7-7ccc-475c-8ec1-40767affe779'), unique=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='student_Ref',
            field=models.UUIDField(default=uuid.UUID('bdfeaa00-d896-4c0d-a7c6-49a9e3d97401'), unique=True),
        ),
    ]
