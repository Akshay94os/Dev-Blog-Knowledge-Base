from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        name = request.POST.get('author_name')
        body = request.POST.get('body')
        if name and body:
            Comment.objects.create(post=post, author_name=name, body=body)
            return redirect('post_detail', slug=post.slug)
    return render(request, 'blog/detail.html', {'post': post})
