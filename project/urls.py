from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', projects, name='projects'),
    path('projects/add/', add_project, name='add-project'),
    path('projects/detail/<uuid:pk>/', project_detail, name='project-detail'),
    path('projects/edit/<uuid:pk>/', edit_project, name='project-edit'),
    path('projects/delete/<uuid:pk>/', delete_project, name='project-delete'),
    path('projects/files/upload_file/<uuid:pk>/', upload_file, name='upload-file'),
    path('projects/notes/add/<uuid:pk>/', add_note, name='add-note'),
    path('projects/<uuid:project_id>/notes/detail/<uuid:pk>/', detail_note, name='detail-note'),
    path('projects/<uuid:project_id>/notes/edit/<uuid:pk>/', edit_note, name='edit-note'),
    path('projects/<uuid:project_id>/notes/delete/<uuid:pk>/', delete_note, name='delete-note'),
    path('projects/<uuid:pk>/files/delete_file/<uuid:file_id>/', delete_file, name='delete-file')
]