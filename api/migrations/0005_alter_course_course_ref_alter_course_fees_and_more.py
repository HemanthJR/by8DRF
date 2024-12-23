# Generated by Django 5.1.4 on 2024-12-12 09:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_course_studentdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_Ref',
            field=models.UUIDField(default=uuid.UUID('d87d7875-61b5-44df-9938-e5c3fd6f68fd'), unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='student_Ref',
            field=models.UUIDField(default=uuid.UUID('9b2111c4-9ec2-49b4-8473-8a3fb3b84009'), unique=True),
        ),
    ]
