from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

def post_handle(request, **kwargs):
    if request.method == 'GET':
        get_post(request, kwargs)

def get_post(request, uri):
    pass

def create_post(request, **kwargs):
    pass

def update_post(request, **kwargs):
    pass

def delete_post(request, uri):
    pass

def list_posts(request):
    if request.method == 'GET':
# don't bother with paging for now
# 1. query all posts
# 2. return a list of post objects to post_list template.
        posts = Post.objects.all()
        print(posts)
        return HttpResponse('hello')

def error(error_code, msg):
    pass

