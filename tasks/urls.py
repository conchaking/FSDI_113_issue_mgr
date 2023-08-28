from django.urls import path
from .views import ListView, CreateView, UpdateView, DeleteView, DetailView

urlpatterns = [
    path("", ListView.as_view(), name="tasks"),
    path("create/", CreateView.as_view(), name="new"),
    path("update/<int:pk>", UpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", DeleteView.as_view(), name="delete"),
    path("detail/<int:pk>", DetailView.as_view(), name="detail"),
]