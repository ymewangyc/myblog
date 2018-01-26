# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# 文章（Post）、分类（Category）以及标签（Tag）

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 创建时间，修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    # 分类只能有一个（一对多），标签可以有多个（多对多）
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    # 文章作者
    author = models.ForeignKey(User)





