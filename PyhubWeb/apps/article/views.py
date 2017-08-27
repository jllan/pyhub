from django.shortcuts import render, redirect, HttpResponseRedirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Articles
# from django.core.paginator import Paginator

def article_index(request):
    articles = Articles.objects.order_by("-pub_date")

    # 分页数据
    try:
        page = int(request.GET.get('page', 1))  # 页码
        paginator = Paginator(articles, 10, request=request)  # 获取有多少页
        articles = paginator.page(page)  # 获取指定页的数据
    except Exception as e:
        return HttpResponseRedirect('/')

    return render(request, 'article/index.html', {
        'articles': articles
    })


def article_tag(request, tag_name):
    articles = Articles.objects.filter(tags=tag_name).order_by("-pub_date")
    try:
        page = int(request.GET.get('page', 1))  # 页码
        paginator = Paginator(articles, 10, request=request)  # 获取有多少页
        articles = paginator.page(page)  # 获取指定页的数据
    except Exception as e:
        return HttpResponseRedirect('/')

    return render(request, 'article/index.html', {
        'articles': articles
    })


def article_search(request,):
    search_for = request.GET['search_for']
    if search_for:
        articles = Articles.objects.filter(title__icontains=search_for).order_by("-pub_date")
        try:
            page = int(request.GET.get('page', 1))  # 页码
            paginator = Paginator(articles, 10, request=request)  # 获取有多少页
            articles = paginator.page(page)  # 获取指定页的数据
        except Exception as e:
            return HttpResponseRedirect('/')

        return render(request, 'article/index.html', {
            'articles': articles
        })
    else:
        return redirect('app:index')


def article_detail(request, article_id):
    article = Articles.objects.filter(id=article_id).first()
    print(article)
    return render(request, 'article/detail.html', {'article':article})


def not_found(request, error):
    return render(request, 'article/404.html')
