from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Projects

# Create your views here.

def index(request):
    projects = Projects.objects
    context = {'projects':projects}
    return render(request,'projects/index.html',context)

def details(request, project_id):
    project_details = get_object_or_404(Projects, pk = project_id)
    context = { 'projects': project_details}
    return render(request, 'projects/details.html', context )

