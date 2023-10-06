from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from . models import task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

def add(request):
    Task1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        Task=task(name=name,priority=priority)
        Task.save()
    return render(request, "home.html",{'Task':Task1})

def delete(request,task_id):
    Task=task.objects.get(id=task_id)
    if request.method=='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    form=TodoForm(request.POST or None , instance=Task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'Task':Task})


class Tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'Task'

class TaskDetailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model= task
    template_name= 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetails',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')