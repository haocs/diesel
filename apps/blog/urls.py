from django.conf.urls import url

from . import views

urlpatterns = [
    # blog_id for get/put/delete
    url(r'^(?P<article_id>[0-9]+)$', views.article_handle),
    # uri could be used for get/put/delete
    url(r'^(?P<uri>[a-z|A-Z|0-9|_]+)$', views.article_handle),
]
