from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Home Page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def add(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)
