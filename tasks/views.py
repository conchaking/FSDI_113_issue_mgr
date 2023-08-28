from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
# Create your views here.
class ListView(ListView):
    template_name = "tasks/list.html"
    model = Task

class DetailView(DetailView):
    template_name = "tasks/detail.html"
    model = Task

class CreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/create.html"
    model = Task
    fields = ["name", "description", "progress"]
    success_url = reverse_lazy("tasks")
    
class UpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/edit.html"
    model = Task
    fields = ["name", "description", "progress"]
    success_url = reverse_lazy("tasks")
    
class DeleteView(LoginRequiredMixin, DeleteView):
    template_name = "tasks/delete.html"
    model = Task
    success_url = reverse_lazy("tasks")

    