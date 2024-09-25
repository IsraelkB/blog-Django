from django.shortcuts import render, get_object_or_404

from .models import Post


def get_date(post):
    return post["date"]


def home(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    id_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": id_post,
        "post_tags": id_post.tags.all(),
    })
