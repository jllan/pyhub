from django.shortcuts import render, redirect, HttpResponseRedirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Questions
# from django.core.paginator import Paginator

def question_index(request):
    questions = Questions.objects.all()

    try:
        page = int(request.GET.get('page', 1))  # 页码
        paginator = Paginator(questions, 10, request=request)  # 获取有多少页
        questions = paginator.page(page)  # 获取指定页的数据
    except Exception as e:
        return HttpResponseRedirect('/')

    return render(request, 'qa/index.html', {
        'questions': questions
    })


def question_tag(request, tag_name):
    questions = Questions.objects.filter(tags=tag_name)
    try:
        page = int(request.GET.get('page', 1))  # 页码
        paginator = Paginator(questions, 10, request=request)  # 获取有多少页
        questions = paginator.page(page)  # 获取指定页的数据
    except Exception as e:
        return HttpResponseRedirect('/')

    return render(request, 'qa/index.html', {
        'questions': questions
    })


def question_search(request,):
    search_for = request.GET['search_for']
    if search_for:
        questions = Questions.objects.filter(title__icontains=search_for)
        context = {
            'questions': questions,
        }
        return render(request, 'qa/index.html', context)
    else:
        return redirect('app:index')


def question_detail(request, question_id):
    question = Questions.objects.filter(id=question_id).first()
    return render(request, 'qa/detail.html', {'question':question})


def not_found(request, error):
    return render(request, 'qa/404.html')
