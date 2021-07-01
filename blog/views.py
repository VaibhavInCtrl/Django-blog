import django
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.


class PostClassView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'pp'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostClassView(ListView):
    model = Post
    template_name = 'user_post.html'
    context_object_name = 'pp'
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateForm(LoginRequiredMixin, CreateView):
    
    model= Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateForm(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/blog'
    template_name = 'post_delete.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False
    
    
    
def home(request):
    content = {"pp":Post.objects.all()}
    return render(request, "home.html",content)

def detail(request):
    return render(request,"detail.html",{"title":"Detail"})