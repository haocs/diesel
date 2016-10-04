from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_posts),
    url(r'^', views.create_post)
]