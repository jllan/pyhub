from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'qa'
urlpatterns = [
    url(r'^$', views.question_index, name='index'),
    url(r'^qa/$', views.question_index, name='index'),
    url(r'^qa/detail/(?P<question_id>\w+)$', cache_page(60 * 15)(views.question_detail), name='detail'),
    url(r'^qa/search/$', views.question_search, name='search'),
    url(r'^qa/tag/(?P<tag_name>.+)$', views.question_tag, name='tag'),
]