from django.shortcuts import render
import datetime
from .models import Post, Author
from django.http import HttpResponse

# Create your views here.

def test(request):
    t = datetime.datetime.now()
    return render(request, 'test.html', {"current_time":t})

def posts(request):
    posts = Post.objects.all()

    return render(request, 'posts.html', {"posts":posts})

def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        post = ""
    return render(request, 'post.html', {"post":post})