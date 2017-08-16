from django.shortcuts import render, redirect
from .models import Articles
# from django.core.paginator import Paginator

def article_index(request):
    articles = Articles.objects
    context = {
        'articles': articles,
    }
    return render(request, 'article/index.html', context)

def article_tag(request, tag_name):
    articles = Articles.objects.filter(tags=tag_name)
    context = {
        'articles': articles,
    }
    return render(request, 'article/index.html', context)


def article_search(request,):
    search_for = request.GET['search_for']
    if search_for:
        articles = Articles.objects.filter(title__icontains=search_for)
        context = {
            'articles': articles,
        }
        return render(request, 'article/index.html', context)
    else:
        return redirect('app:index')


def article_detail(request, article_id):
    article = Articles.objects.filter(id=article_id).first()
    return render(request, 'article/detail.html', {'article':article})


def not_found(request, error):
    return render(request, 'article/404.html')
