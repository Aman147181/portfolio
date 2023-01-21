from django.shortcuts import render, get_object_or_404,redirect
from .models import Projects,Comment
from .forms import CommentForm

def project_detail(request, pk):
  project = get_object_or_404(Projects, pk=pk)
  comments = Comment.objects.filter(project=project)
  return render(request, 'project.html', {'project': project, 'comments': comments})
  

def home(request):
    projects = Projects.objects.filter(ispopolar=True)
    return render(request,'home.html', {'projects':projects})

def add_comment(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect('project_detail', pk=pk)
    else: 
        form = CommentForm()
    return render(request, 'project.html', {'form': form})