from django.shortcuts import render, redirect, HttpResponseRedirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Jobs
# from django.core.paginator import Paginator

def job_index(request):
    jobs = Jobs.objects.order_by("-pub_time")

    try:
        page = int(request.GET.get('page', 1))  # 页码
        paginator = Paginator(jobs, 10, request=request)  # 获取有多少页
        jobs = paginator.page(page)  # 获取指定页的数据
    except Exception as e:
        return HttpResponseRedirect('/')

    return render(request, 'job/index.html', {
        'jobs': jobs
    })


def job_search(request,):
    search_for = request.GET['search_for']
    if search_for:
        jobs = Jobs.objects.filter(title__icontains=search_for).order_by("-pub_time")
        context = {
            'jobs': jobs,
        }
        return render(request, 'job/index.html', context)
    else:
        return redirect('app:index')


def job_detail(request, job_id):
    job = Jobs.objects.filter(position_id=job_id).first()
    return render(request, 'job/detail.html', {'job': job, 'job_detail': ''.join(job.job_detail)})


def not_found(request, error):
    return render(request, 'job/404.html')
