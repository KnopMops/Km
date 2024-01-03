from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from todolist.models import *
from task.models import *


@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    projects_length = len(projects)
    context = {
        'projects': projects,
        'projects_length': projects_length
    }

    return render(request, 'project/projects.html', context)


@login_required
def project_detail(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    todolists = Todolist.objects.all()
    todolists_length = len(todolists)
    context = {
        'project': project,
        'todolists_length': todolists_length
    }

    return render(request, 'project/project_detail.html', context)


@login_required
def add_project(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name and description:
            project = Project.objects.create(name=name, description=description, created_by=request.user)
            return redirect('projects')

    return render(request, 'project/add_project.html')


@login_required
def edit_project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name and description:
            project.name = name
            project.description = description
            project.save()

            return redirect('projects')

    context = {
        'project': project
    }

    return render(request, 'project/edit_project.html', context)


@login_required
def delete_project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    project.delete()
    return redirect('projects')


@login_required
def upload_file(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProjectFileForm(request.POST, request.FILES)
        if form.is_valid():
            projectfile = form.save(commit=False)
            projectfile.project = project
            projectfile.save()
            return redirect(f'/api/v1/management/projects/detail/{pk}/')

    form = ProjectFileForm()
    context = {
        'project': project,
        'form': form
    }

    return render(request, 'project/upload/upload_file.html', context)


@login_required
def delete_file(request, pk, file_id):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    projectfile = project.files.get(pk=file_id)
    projectfile.delete()
    return redirect(f'/api/v1/management/projects/detail/{pk}/')


@login_required
def add_note(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        body = request.POST.get('body', '')

        if name and body:
            ProjectNote.objects.create(project=project, name=name, body=body)
            return redirect(f'/api/v1/management/projects/detail/{pk}/')

    context = {
        'project': project
    }

    return render(request, 'project/note/add_note.html', context)


@login_required
def detail_note(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    note = project.notes.get(pk=pk)
    context = {
        'project': project,
        'note': note
    }

    return render(request, 'project/note/detail_note.html', context)


@login_required
def edit_note(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    note = project.notes.get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        body = request.POST.get('body', '')

        if name and body:
            note.name = name
            note.body = body
            note.save()

            return redirect(f'/api/v1/management/projects/{project_id}/notes/detail/{pk}/')

    context = {
        'project': project,
        'note': note
    }

    return render(request, 'project/note/edit_note.html', context)


@login_required
def delete_note(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    note = project.notes.get(pk=pk)
    note.delete()
    return redirect(f'/api/v1/management/projects/detail/{project_id}')