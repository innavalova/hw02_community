from django.shortcuts import get_object_or_404, render

from .models import Group, Post


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
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
