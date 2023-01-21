from django.shortcuts import render, get_object_or_404,redirect
from .models import Projects

def project_detail(request, pk):
  project = get_object_or_404(Projects, pk=pk)
  return render(request, 'project.html', {'project': project})
  

def home(request):
    projects = Projects.objects.filter(ispopolar=True)
    return render(request,'home.html', {'projects':projects})
