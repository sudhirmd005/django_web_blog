from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse, Http404
from .models import Post
from django.utils import timezone
from .form import PostForm

def post_line(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_line.html', {'posts': posts})
def post_details(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'posts': posts})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})