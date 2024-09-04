from datetime import date
from django.utils.text import slugify
from django.shortcuts import render

all_posts = [
    {
        "slug": "java",
        "image": "about.png",
        "author": "Israel Kabesa",
        "date": date.today(),
        "title": "Java Tools",
        "excerpt": "There's nothing like the feeling of finishing your first Big Project, and creating new application",
        "content": """in our BattleWord Application we used a lot of Java for generating the Automatic CrossWord 
        Generator by Using Java language."""
    },
    {
        "slug": "react",
        "image": "BattleWord.png",
        "author": "Israel Kabesa",
        "date": date.today(),
        "title": "TS and React Tools",
        "excerpt": "There's nothing like the feeling of finishing your first Big Project, and creating new application",
        "content": """in our BattleWord Application we used a lot of React and TypeScript for generating the
         Frontend of our BattleWord project."""
    },
    {
        "slug": "python",
        "image": "GameMode.png",
        "author": "Israel Kabesa",
        "date": date.today(),
        "title": "Python Tools",
        "excerpt": "There's nothing like the feeling of finishing your first Big Project, and creating new application",
        "content": """in our BattleWord Application we used a lot of Python for generating the BeckEnd of our BattleWord 
        project, by Using Django framework."""
    }
]



# Create your views here.


def get_date(post):
    return post["date"]


def home(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    id_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": id_post
    })
