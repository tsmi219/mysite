from django.shortcuts import render, get_object_or_404
from .models import Post #"look inside models directory for Post"
from .forms import PostForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# create way for a user to make their own post with logi as well
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm() # if form not done right, load blank form
    return render(request, 'blog/post_edit.html', {'form': form})

# allow users to edit posts
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
