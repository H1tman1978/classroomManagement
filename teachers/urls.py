from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='teacher_index'),
    path('<int:pk>', views.detail_view, name='teacher_detail'),
]
