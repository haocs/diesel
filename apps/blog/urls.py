from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)$', views.post_handle),
    # uri could be used for get/put/delete
    url(r'^(?P<uri>[a-z|A-Z|0-9|_]+)$', views.post_handle),
]
