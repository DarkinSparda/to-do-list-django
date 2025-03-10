from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def list(request):
    page = 'base/task_list.html'

    if request.method == 'GET':
        task_list = Task.objects.all()
        
        if request.user.is_authenticated:
            task_list = Task.objects.filter(owner=request.user)

        context = {
            'task_list' : task_list
        }
        return render(request, page, context)
    
    
def register(request):
    page = 'base/register.html'
    # POST
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print('valid')
            user = form.save(commit=False)
            user.save()
            return redirect('list')
        else:
            messages.error(request, 'There was an error with your submission.')
            return render(request, page, {'form': form})

    # GET
    else:
        if request.user.is_authenticated:
            return redirect('list')
        form = UserForm()
        return render(request, page, {'form' : form}) 
    

def login_view(request):
    page = 'base/login.html'
    # POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("user is valid")
            login(request, user)
            return redirect('list')
        else:
            return render(request, page, {'error': 'Invalid username or password'})
        

    # GET
    else:
        if request.user.is_authenticated:
            return redirect('list')
        return render(request, page)

@login_required(login_url='/login')
def create(request):
    page = 'base/task_form.html'
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print('form is valid')
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('list')
        else:
            context = {'form' : form}
            return render(request, page, context)
    else:
        form = TaskForm()
    
    return render(request, page, {'form' : form})
@login_required(login_url='/login')
def update(request, pk):
    page = 'base/task_form.html'
    
    if request.method == 'POST':
        task = Task.objects.get(owner = request.user, id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request, page, {'form': form})
    else:
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
    


    return render(request, page, {'form': form})
@login_required(login_url='/login')
def delete(request, pk):
    page = 'base/task_confirm_delete.html'
    task = Task.objects.get(owner=request.user, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
 
    return render(request, page, {'task': task})

def logout_view(request):
    logout(request)
    return redirect('list')