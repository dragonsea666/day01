

from django.conf.urls import url
from backweb import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('art', views.Articleview)


urlpatterns = [

    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^flink/', views.flink),
    url(r'^loginlog', views.loginlog),
    url(r'^article/', views.article, name='article'),
    url(r'^category/', views.category),
    url(r'^comment/', views.comment),
    url(r'^add_article/', views.add_article),
    url(r'^add_flink/', views.add_flink),
    url(r'^add_notice/', views.add_notice),
    url(r'^manage_user', views.manage_user),
    url(r'^notice/', views.notice),
    url(r'^readset/', views.readset),
    url(r'^setting/', views.setting),
    url(r'^update_article/', views.update_article, name='update_article'),
    url(r'^update_category/', views.update_category),
    url(r'^update_flink/', views.update_flink),
    url(r'^update-article/(\d+)/', views.updatearticle, name='updatearticle'),
]

urlpatterns += router.urls

