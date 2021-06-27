from django.shortcuts import render
from .models import Post
# Create your views here.



def home(request):
    content = {"pp":Post.objects.all()}
    return render(request, "home.html",content)

def detail(request):
    return render(request,"detail.html",{"title":"Detail"})