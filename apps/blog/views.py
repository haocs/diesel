from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Tag

import json


@csrf_exempt
def post_handle(request, **kwargs):
    if request.method == 'GET':
        return get_post(request, **kwargs)
    elif request.method == 'POST':
         return create_post(request, **kwargs)
    elif request.method == 'PUT':
        update_post(request, **kwargs)
    elif request.method == 'DELETE':
        pass

def get_post(request, **kwargs):
    return HttpResponse('ok')

def create_post(request, **kwargs):
    if not request.body:
        return HttpResponse('error')
    print(kwargs.get('uri'))
    print(kwargs.get('post_id'))
    post_json = json.loads(request.body.decode('utf-8'))
    print(post_json)
    print(type(post_json))
    title = post_json.get('title')
    content = post_json['title']
    tags = post_json.get('tags')
    return HttpResponse('ok')

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

