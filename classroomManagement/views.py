from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from .settings import SCHOOL_NAME, SCHOOL_MASCOT


def welcome_view(request):
    number_of_students = Student.objects.count()
    number_of_teachers = Teacher.objects.count()
    school_name = SCHOOL_NAME
    mascot = SCHOOL_MASCOT
    context = {
        'number_of_students': number_of_students,
        'number_of_teachers': number_of_teachers,
        'school_name': school_name,
        'mascot': mascot
    }
    return render(request, 'welcome.html', context)
