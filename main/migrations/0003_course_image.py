# Generated by Django 5.1 on 2024-08-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_group_lesson_groupstudents_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
