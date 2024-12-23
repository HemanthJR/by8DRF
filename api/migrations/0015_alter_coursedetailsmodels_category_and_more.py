# Generated by Django 5.1.4 on 2024-12-13 07:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_coursedetailsmodels_course_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetailsmodels',
            name='category',
            field=models.CharField(blank=True, choices=[('basic', 'basic'), ('advanced', 'advanced'), ('placement', 'placement')], null=True),
        ),
        migrations.AlterField(
            model_name='coursedetailsmodels',
            name='course_Ref',
            field=models.UUIDField(default=uuid.UUID('79146ed2-586e-49f7-9df7-b351ff38ff3d'), unique=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodels',
            name='student_Organization',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetailsmodels',
            name='student_Ref',
            field=models.UUIDField(default=uuid.UUID('e1f03003-8b0a-4b07-aeef-a1e9708276f8'), unique=True),
        ),
    ]
