# conding: utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
'''
def index(request):
    return HttpResponse("欢迎访问我的博客首页！")


def index(request):
    return render(request,'blog/index.html',context={
        'title':'我的博客首页',
        'welcome':'欢迎访问我的博客首页'
    })
'''
from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})