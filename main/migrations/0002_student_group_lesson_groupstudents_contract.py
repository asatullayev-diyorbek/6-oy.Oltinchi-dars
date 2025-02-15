# Generated by Django 5.1 on 2024-08-22 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
            ],
            options={
                'verbose_name': "O'quvchi",
                'verbose_name_plural': "O'quvchilar",
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
            options={
                'verbose_name': 'Guruh',
                'verbose_name_plural': 'Guruhlar',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.group')),
            ],
            options={
                'verbose_name': 'Dars',
                'verbose_name_plural': 'Darslar',
            },
        ),
        migrations.CreateModel(
            name='GroupStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_status', models.BooleanField(default=False)),
                ('reg_date', models.DateField()),
                ('end_date', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.group')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name': "Guruh o'quvchisi",
                'verbose_name_plural': "Guruh o'quvchilari",
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contract_number', models.CharField(max_length=100)),
                ('add_date', models.DateField()),
                ('end_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
            options={
                'verbose_name': 'Shartnoma',
                'verbose_name_plural': 'Shartnomalar',
            },
        ),
    ]
