# coding: utf-8
'''
import sys, pprint

pprint.pprint(sys.path)
'''
from blog.models import Category,Post,Tag
# from blog import models

from django.utils import timezone
from django.contrib.auth.models import User

user = User.objects.get(username='x318')
c = Category.objects.get(name='category test')

p = Post(title='title test',body='body test',created_time=timezone.now(),modified_time=timezone.now(),category=c,author=user)
p.save()

