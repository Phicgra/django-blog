from django.shortcuts import render
from .models import Blog_post
# Create your views here.


def index(request):
    post = Blog_post.objects.all().order_by('-time')
    return render(request, 'index.html', {'post':post})


def allposts(request, pd):
    post = Blog_post.objects.get(id=pd)
    return render(request, 'allposts.html', {'post':post})
