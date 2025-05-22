from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeUploadForm, ProjectForm
from .models import Project

# @login_required
def profile_view(request):
    projects = Project.objects.filter(user=request.user)
    resume_form = ResumeUploadForm(instance=request.user)

    if request.method == 'POST':
        resume_form = ResumeUploadForm(request.POST, request.FILES, instance=request.user)
        if resume_form.is_valid():
            resume_form.save()
            return redirect('profile')

    return render(request, 'profile.html', {'projects': projects, 'resume_form': resume_form})

# @login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('profile')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})
