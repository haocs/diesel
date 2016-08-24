from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag


def index(request):
    if request.method == 'GET':
        return HttpResponse('hello')


def create_post(request):
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        content = data['content']
        tags = data['tags']
        new_post = Post(title=title, content=content)


def update_post(request):
    pass


def delete_post(request):
    pass


        

