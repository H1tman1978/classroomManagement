# ClassroomManagement/students/views.py
from django.views.generic import ListView, DetailView
from css_grid.views import CSSGridMixin
from .models import Student


class StudentsListView(CSSGridMixin, ListView):
    model = Student
    queryset = Student.objects.order_by('grade_level')
    template_name = 'students/student_index.html'

    grid_wrapper = 'student-wrapper'
    grid_template_columns = ['1fr', '1fr', '1fr']
    grid_template_areas = [
        ['sidebar', 'content'],
        ['sidebar', 'content'],
        ['header', 'header'],
    ]
    grid_gap = '1em'


class StudentDetailView(CSSGridMixin, DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    # Grid details
    grid_wrapper = 'student-wrapper'
    grid_template_columns = ['1fr', '1fr', '1fr']
    grid_template_areas = [
        ['sidebar', 'content'],
        ['sidebar', 'content'],
        ['header', 'header'],
    ]
    grid_gap = '1em'
    # Additional Parameters


"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = Student.objects.pk
        return context
"""
