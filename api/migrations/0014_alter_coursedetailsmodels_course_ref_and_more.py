# Generated by Django 5.1.4 on 2024-12-13 05:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_coursedetailsmodels_studentdetailsmodels_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetailsmodels',
            name='course_Ref',
            field=models.UUIDField(default=uuid.UUID('50b1557a-b0ec-4c7c-b776-51b6419cb4d7'), unique=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodels',
            name='student_Organization',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodels',
            name='student_Other',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodels',
            name='student_Ref',
            field=models.UUIDField(default=uuid.UUID('fc2cf722-1d06-4468-81bb-d2bd58e89e0e'), unique=True),
        ),
    ]