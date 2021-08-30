from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group}'
    posts = group.groups.all()[:10]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
