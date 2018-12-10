from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import mixins, viewsets
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response

from myapp.article_filter import ArticleFilter
from myapp.articleserializer import ArticleSerializer
from myapp.models import Article, Category


class Articleview(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin,
             mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # 过滤
    filter_class = ArticleFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            data = {}
            data['code'] = 500
            data['msg'] = '获取数据失败'
            return Response(data)

def index(request):

    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        category = Category.objects.all()
        paginator = Paginator(articles, 18)
        c = Paginator(category, 18)
        cpage = c.page(1)
        page = paginator.page(page)
        return render(request,'./myapp/index.html', {'page': page, 'cpage': cpage})



def about(request):
    if request.method == 'GET':
        category = Category.objects.all()
        c = Paginator(category, 18)
        cpage = c.page(1)
        return render(request,'./myapp/about.html', {'cpage': cpage})

def myabout(request, id=0):
    if request.method == 'GET':
        if id:
            page = int(request.GET.get('page', 1))
            article = Article.objects.filter(c_id=id)
            a_p = Paginator(article, 12)
            page = a_p.page(page)
            category = Category.objects.all()
            c = Paginator(category, 18)
            cpage = c.page(1)
            return render(request, './myapp/about.html', {'page': page, 'cpage': cpage})
        else:
            return render(request, './myapp/about.html')


def gbook(request):

    if request.method == 'GET':
        category = Category.objects.all()
        c = Paginator(category, 18)
        cpage = c.page(1)
        return render(request,'./myapp/gbook.html', {'cpage': cpage})

def myinfo(request, id=0):
    if request.method == 'GET':

        if id:
            article = Article.objects.filter(pk=id).first()
            category = Category.objects.all()
            c = Paginator(category, 18)
            cpage = c.page(1)

            return render(request,'./myapp/info.html', {'article': article, 'cpage':cpage})
        else:
            return render(request, './myapp/info.html')

def info(request):

    if request.method == 'GET':
        category = Category.objects.all()
        c = Paginator(category, 18)
        cpage = c.page(1)
        return render(request,'./myapp/info.html', {'cpage': cpage})



def infopic(request):

    if request.method == 'GET':
        category = Category.objects.all()
        c = Paginator(category, 18)
        cpage = c.page(1)
        return render(request,'./myapp/infopic.html', {'cpage': cpage})

def list(request):

    if request.method == 'GET':
        category = Category.objects.all()
        c = Paginator(category, 18)
        cpage = c.page(1)
        return render(request,'./myapp/list.html', {'cpage': cpage})

def share(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        article = Article.objects.all()
        a_paginator = Paginator(article, 16)
        page = a_paginator.page(page)
        return render(request,'./myapp/share.html', {'page': page})

