from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.models import *
from task.models import *
from .models import *


@login_required
def todolist(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    tasks = Task.objects.all()
    tasks_length = len(tasks)
    context = {
        'project': project,
        'todolist': todolist,
        'tasks_length': tasks_length
    }

    return render(request, 'todolist/detail_todolist.html', context)


@login_required
def edit_todolist(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name and description:
            todolist.name = name
            todolist.description = description
            todolist.save()

            return redirect(f'/api/v1/projects/{project_id}/todolists/{pk}/')

    context = {
        'project': project,
        'todolist': todolist
    }

    return render(request, 'todolist/edit_todolist.html', context)


@login_required
def add_todolist(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name and description:
            todolist = Todolist.objects.create(project=project, name=name, description=description, created_by=request.user)
            return redirect(f'/api/v1/management/projects/detail/{project_id}/')

    return render(request, 'todolist/add_todolist.html')


@login_required
def delete_todolist(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    todolist.delete()
    return redirect(f'/api/v1/management/projects/detail/{project_id}/')