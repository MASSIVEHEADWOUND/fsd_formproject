from django.shortcuts import render
from django.http import HttpResponse
from .forms import projectForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def addProject(request):
    if(request.method=='GET'):
        form = projectForm(request.GET)
        if(form.is_valid()):
            form.save()
            return render(request, 'added.html')
        else:
            form = projectForm()

    else:
        form = projectForm()
    
    return render(request, 'add_project.html',{'form':form})

def viewProject(request):
    pass

def editProject(request):
    pass
