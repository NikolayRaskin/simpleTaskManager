from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from rest_framework import viewsets
from .models import UserMy,Project,Task
from .serializers import UserMySerializer, ProjectSerializer, TaskSerializer
from .forms import AddTaskForm
import datetime

class UserView(viewsets.ModelViewSet):
    queryset = UserMy.objects.all()
    serializer_class = UserMySerializer
    
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

def main(request):
    taskskQuery = Task.objects.all()
    usersQuery = UserMy.objects.all()
    serializer_class = TaskSerializer
    context = {
        'taskskQuery':taskskQuery,
        'usersQuery':usersQuery,
    }
    return render(request,'mainPage/mainPage.html',context)

def addTaskForm(request):
    form = AddTaskForm(request.POST)
    if form.is_valid():
        form.save()
        form = AddTaskForm()
        return redirect('mainPage')
    else:
        print('Form is valid!')
    context = {
        'form':form
    }
    return render(request,'mainPage/form.html',context)

def deleteTask_view(request):
    task_id = request.GET.get('item_task_id')
    task = Task.objects.get(pk=task_id)
    print(Task.objects.count())
    task.delete()
    return JsonResponse({
        'task_count':Task.objects.count()
    })
    #return redirect('mainPage')

def editTask_view(request,task_id):
    task = Task.objects.get(pk=task_id)
    form = AddTaskForm(request.POST,instance=task)
    if form.is_valid():
        form.save()
        return redirect('mainPage')
    else:
        print('Form is valid!')
    context = {
        'form':form
    }
    return render(request,'mainPage/form.html',context)

def compliteTask_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = True
    task.save()
    return redirect('mainPage')
