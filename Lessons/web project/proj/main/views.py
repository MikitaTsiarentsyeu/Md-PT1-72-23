from django.shortcuts import render
import datetime
from .models import Post, Author

# Create your views here.

def test(request):
    t = datetime.datetime.now()
    return render(request, 'test.html', {"current_time":t})

def posts(request):
    posts = Post.objects.all()
    titles = ""
    for p in posts:
        titles = f"{titles} {p.title}"
    return render(request, 'posts.html', {"posts_titles":titles})

def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        title = post.title
    except:
        title = "was not found"
    return render(request, 'posts.html', {"posts_titles":title})