from django.urls import path
from students.views import StudentsListView, StudentDetailView

urlpatterns = [
    path("", StudentsListView.as_view()),
    path("<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
]