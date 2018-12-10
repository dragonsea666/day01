
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from myapp import views
router = SimpleRouter()
router.register('art', views.Articleview)
urlpatterns = [
    # 博客首页
    # 127.0.0.1:8090/web/index/
    url(r'^index/', views.index, name='index'),
    url(r"^about/", views.about),
    url(r'^gbook/', views.gbook),
    url(r'^info/', views.info, name='info'),
    url(r'^infopic/', views.infopic),
    url(r'^list/', views.list),
    url(r'^share/', views.share, name='share'),
    # url(r'^search/', views.search),
    url(r'^myinfo/(\d+)/', views.myinfo, name='myinfo'),
    url(r'^myabout/(\d+)/', views.myabout, name='myabout'),

]
urlpatterns += router.urls