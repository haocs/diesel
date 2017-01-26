from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article, Tag

import json


@csrf_exempt
def article_handle(request, **kwargs):
    if request.method == 'GET':
        return get_article(request, **kwargs)
    elif request.method == 'POST':
        return create_article(request, **kwargs)
    elif request.method == 'PUT':
        return update_article(request, **kwargs)
    elif request.method == 'DELETE':
        pass

def get_article(request, **kwargs):
    return HttpResponse('ok')

def create_article(request, **kwargs):
    if not request.body:
        return HttpResponse('error')
    print(kwargs.get('uri'))
    print(kwargs.get('article_id'))
    article_json = json.loads(request.body.decode('utf-8'))
    print(article_json)
    print(type(article_json))
    title = article_json.get('title')
    content = article_json['title']
    tags = article_json.get('tags')
    return HttpResponse('ok')

def update_article(request, **kwargs):
    pass

def delete_article(request, uri):
    pass

def list_articles(request):
    if request.method == 'GET':
# don't bother with paging for now
# 1. query all articles
# 2. return a list of article objects to article_list template.
        articles = article.objects.all()
        print(articles)
        return HttpResponse('hello')

def error(error_code, msg):
    pass

