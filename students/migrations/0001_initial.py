# Generated by Django 2.2.4 on 2019-08-22 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('assignments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(help_text="Student's School ID", max_length=15, unique=True)),
                ('first_name', models.CharField(help_text="Student's first name", max_length=20)),
                ('last_name', models.CharField(help_text="Student's last name", max_length=20)),
                ('grade_level', models.IntegerField(choices=[('K', 'Kindergarten'), ('1', 'First Grade'), ('2', 'Second Grade'), ('3', 'Third Grade'), ('4', 'Fourth Grade'), ('5', 'Fifth Grade'), ('6', 'Sixth Grade'), ('7', 'Seventh Grade'), ('8', 'Eighth Grade'), ('9', 'Ninth Grade'), ('10', 'Tenth Grade'), ('11', 'Eleventh Grade'), ('12', 'Twelfth Grade')], default='K')),
                ('phone_number', phone_field.models.PhoneField(help_text="Student's contact phone number", max_length=31)),
                ('email', models.EmailField(help_text="Student's email address", max_length=254)),
                ('birthday', models.DateField(default='2000-01-01')),
                ('student_photo', models.ImageField(upload_to='')),
                ('assigned_assignments', models.ManyToManyField(related_name='assignments', to='assignments.Assignment')),
                ('assigned_teachers', models.ManyToManyField(related_name='teachers', to='teachers.Teacher')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
