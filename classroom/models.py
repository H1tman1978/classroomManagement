from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from phone_field import PhoneField
from classroom.contentsettings import *


# Create your models here.
# TODO: Create Teacher Class
class Teacher(models.Model):
    pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=15, unique=True, help_text="Student's School ID")
    first_name = models.CharField(max_length=20, help_text="Student's first name")
    last_name = models.CharField(max_length=20, help_text="Student's last name")
    grade_level = models.IntegerField(default='K', choices=YEAR_IN_SCHOOL_CHOICES)
    phone_number = PhoneField(help_text="Student's contact phone number")
    email = models.EmailField(max_length=254, help_text="Student's email address")
    birthday = models.DateField(auto_now_add=False, auto_now=False, default='2000-01-01')
    student_photo = models.ImageField()
    assigned_teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.profile.save()


# TODO: Create Assignment class
class Assignment(models.Model):
    pass


# TODO: Create Question class
class Question(models.Model):
    pass


# TODO: Create Answer class