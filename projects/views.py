from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.get(title='E-Commerce')
    return HttpResponse(projects.tags.all())


def project(request, pk):
    projects = Project.objects.get(title='E-Commerce')
    return HttpResponse(projects.review_set.all())


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    
    return HttpResponse('created Done!')


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('')
    
    return HttpResponse('created Done!')


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('')
    
    return HttpResponse('Deleted')