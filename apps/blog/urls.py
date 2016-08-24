from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'', views.index),
    url(r'^create', views.create_post),
    url(r'^update', views.update_post),
    url(r'^delete', views.delete_post)
]