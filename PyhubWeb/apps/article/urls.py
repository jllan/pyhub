from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'article'
urlpatterns = [
    # url(r'^$', views.question_index, name='index'),
    url(r'^article/$', views.article_index, name='index'),
    url(r'^article/detail/(?P<article_id>\w+)$', cache_page(60 * 15)(views.article_detail), name='detail'),
    url(r'^article/search/$', views.article_search, name='search'),
    url(r'^article/tag/(?P<tag_name>.+)$', views.article_tag, name='tag'),
]