from django.urls import path
from .views import *

urlpatterns = [
    path('todolists/add/', add_todolist, name='add_todolist'),
    path('todolists/edit/<uuid:pk>/', edit_todolist, name='edit_todolist'),
    path('todolists/delete/<uuid:pk>/', delete_todolist, name='delete_todolist'),
    path('todolists/<uuid:pk>/', todolist, name='detail_todolist')
]