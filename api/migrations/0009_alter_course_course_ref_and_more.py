# Generated by Django 5.1.4 on 2024-12-12 09:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_course_course_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_Ref',
            field=models.UUIDField(default=uuid.UUID('0f7e7872-de66-4a57-8774-8cd3bdb8c911'), unique=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='student_Ref',
            field=models.UUIDField(default=uuid.UUID('58dcbfb7-abad-46c3-867e-20f010c6820f'), unique=True),
        ),
    ]
