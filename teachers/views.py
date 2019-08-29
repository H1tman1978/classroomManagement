from django.shortcuts import render
from .models import Teacher


# Create your views here.
def index(request):
    teacher_list = Teacher.objects.order_by('last_name')
    context = {
        'teacher_list': teacher_list,
    }
    return render(request, 'teachers/teacher_index.html', context)


def detail_view(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    context = {
        'teacher': teacher
    }
    return render(request, 'teachers/teacher_detail.html', context)
