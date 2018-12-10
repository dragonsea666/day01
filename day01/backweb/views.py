from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.response import Response

from backweb.Artform import AddArtForm, EditArtForm
from backweb.article_filter import ArticleFilter
from backweb.articleserializer import ArticleSerializer
from backweb.models import User
from rest_framework import mixins, viewsets
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
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

    # if request.method == 'GET':
    return render(request,'./backweb/index.html')
    # return HttpResponse('令牌')

def login(request):
    if request.method == 'GET':
        return render(request,'./backweb/login.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        if not username:
            err_name = '账号不能为空'
            return render(request, './backweb/login.html', {'err_name': err_name})
        user = User.objects.filter(username=username).first()
        if not password:
            err_pwd = '密码不能为空'
            return render(request, './backweb/login.html', {'err_pwd': err_pwd})
        if user:
            check_pass = check_password(password,user.password)
            if check_pass:
                res = HttpResponseRedirect('/backweb/index/')
                request.session['user_id'] = user.id
                return res
            else:
                err_pwd = '密码错误'
                return render(request, './backweb/login.html', { 'err_pwd': err_pwd })
        else:
            err_name = '账号不存在'
            return render(request, './backweb/login.html', {'err_name': err_name})


def flink(request):

    # if request.method == 'GET':
    return render(request,'./backweb/flink.html')

def loginlog(request):

    # if request.method == 'GET':
    return render(request,'./backweb/loginlog.html')




def article(request):

    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 6)
        page = paginator.page(page)

        return render(request,'./backweb/article.html', {'page': page})


def category(request):

    # if request.method == 'GET':
    return render(request,'./backweb/category.html')

def comment(request):

    # if request.method == 'GET':
    return render(request,'./backweb/comment.html')

def add_article(request):

    if request.method == 'GET':
        return render(request,'./backweb/add-article.html')

    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            titlepic = form.cleaned_data['titlepic']
            keywords = form.cleaned_data['keywords']
            category = form.cleaned_data['category']
            cat = Category.objects.filter(c_name=category).first()
            if cat:
                Article.objects.create(title=title, a_content=content, a_keyword=keywords, a_describe=describe, icon=titlepic, c=cat)
                return HttpResponseRedirect('/backweb/index/')
            form = '没有这个种类的分类'
            return render(request, './backweb/add-article.html', {'form': form})

        else:
            print(request.POST.get('category'))
            return render(request, './backweb/add-article.html', {'form': form})

def add_flink(request):

    # if request.method == 'GET':
    return render(request,'./backweb/add-flink.html')

def add_notice(request):

    # if request.method == 'GET':
    return render(request,'./backweb/add-notice.html')

def manage_user(request):

    # if request.method == 'GET':
    return render(request,'./backweb/manage-user.html')

def notice(request):

    # if request.method == 'GET':
    return render(request,'./backweb/notice.html')

def readset(request):

    # if request.method == 'GET':
    return render(request,'./backweb/readset.html')

def setting(request):

    # if request.method == 'GET':
    return render(request,'./backweb/setting.html')

def update_article(request):

    # if request.method == 'GET':
    return render(request,'./backweb/update-article.html')

def update_category(request):

    # if request.method == 'GET':
    return render(request,'./backweb/update-category.html')

def update_flink(request):

    # if request.method == 'GET':
    return render(request,'./backweb/update-flink.html')

def updatearticle(request, id):

    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()

        return render(request,'./backweb/update-article.html', {'article': article})

    if request.method == 'POST':
        form = EditArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            describe = form.cleaned_data['describe']
            content = form.cleaned_data['content']
            titlepic = form.cleaned_data['titlepic']
            keywords = form.cleaned_data['keywords']
            category = form.cleaned_data['category']
            cat = Category.objects.filter(c_name=category).first()
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.a_describe = describe
            article.a_content = content
            article.a_keyword = keywords
            if cat:
                article.c = cat
            if titlepic:
                article.icon = titlepic
            article.save()

            return HttpResponseRedirect(reverse('backweb:article'))

        else:
            return render(request, './backweb/update-article.html', {'form': form})


