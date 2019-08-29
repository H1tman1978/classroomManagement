from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField
from contentsettings import *
from teachers.models import Teacher
from assignments.models import Assignment


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_users")
    student_id = models.CharField(max_length=15, unique=True, help_text="Student's School ID")
    first_name = models.CharField(max_length=20, help_text="Student's first name")
    last_name = models.CharField(max_length=20, help_text="Student's last name")
    grade_level = models.CharField(default='K', choices=YEAR_IN_SCHOOL_CHOICES, max_length=2)
    phone_number = PhoneField(help_text="Student's contact phone number")
    email = models.EmailField(max_length=254, help_text="Student's email address")
    birthday = models.DateField(auto_now_add=False, auto_now=False, default='2000-01-01')
    photo = models.ImageField(upload_to='images/')
    assigned_teachers = models.ManyToManyField(Teacher, related_name="teachers", blank=True)
    assigned_assignments = models.ManyToManyField(Assignment, related_name="assignments", blank=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.student_id)])


'''
@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)




@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
