from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'job'
urlpatterns = [
    # url(r'^$', views.question_index, name='index'),
    url(r'^$', views.job_index, name='index'),
    url(r'^detail/(?P<job_id>\w+)$', cache_page(60 * 15)(views.job_detail), name='detail'),
    url(r'^search/$', views.job_search, name='search'),
]