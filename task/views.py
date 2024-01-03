from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.models import *
from todolist.models import *
from .models import *


@login_required
def add_task(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        task = Task.objects.create(project=project, todolist=todolist, name=name, description=description, created_by=request.user)
        return redirect(f'/api/v1/projects/{project_id}/todolists/{todolist_id}/')
    
    return render(request, 'task/add_task.html')


@login_required
def detail_task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task  = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.GET.get('is_done', '') == 'yes':
        task.is_done = True
        task.save()

    elif request.GET.get('is_done', '') == 'no':
        task.is_done = False
        task.save()

    context = {
        'task': task
    }

    return render(request, 'task/detail_task.html', context)


@login_required
def edit_task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task  = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name and description:
            task.name = name
            task.description = description
            task.save()

            return redirect(f'/api/v1/projects/{project_id}/{todolist_id}/tasks/detail/{pk}/')
        
    context = {
        'task': task
    }
        
    return render(request, 'task/edit_task.html', context)


@login_required
def delete_task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task  = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    task.delete()
    return redirect(f'/api/v1/projects/{project_id}/todolists/{todolist_id}/')