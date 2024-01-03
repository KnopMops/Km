from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/detail/<uuid:pk>/', detail_task, name='detail_task'),
    path('tasks/edit/<uuid:pk>/', edit_task, name='edit_task'),
    path('tasks/delete/<uuid:pk>/', delete_task, name='delete_task')
]