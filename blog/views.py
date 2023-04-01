from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.


class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailPage(DetailView):
    model = Post
    template_name = 'detailPage.html'


class NewPostPage(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ["title", "author", "body"]


class EditPostPage(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ["title", "body"]

class DeletePostPage(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("home")
