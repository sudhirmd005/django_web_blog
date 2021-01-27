from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from .models import Post
from django.utils import timezone

def post_line(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_line.html', {'posts': posts})
def post_details(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'posts': posts})
