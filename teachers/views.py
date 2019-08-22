from django.shortcuts import render
from .models import Teacher


# Create your views here.
def index(request):
    teacher_list = Teacher.objects.order_by('last_name')
    context = {
        'teacher_list': teacher_list,
    }

    return render(request, 'teacher_index.html', context)
