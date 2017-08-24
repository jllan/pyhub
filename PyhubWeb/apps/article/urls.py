from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'article'
urlpatterns = [
    # url(r'^/$', views.question_index, name='index'),
    url(r'^$', views.article_index, name='index'),
    url(r'^detail/(?P<article_id>\w+)$', cache_page(60 * 15)(views.article_detail), name='detail'),
    url(r'^search/$', views.article_search, name='search'),
    url(r'^tag/(?P<tag_name>.+)$', views.article_tag, name='tag'),
]