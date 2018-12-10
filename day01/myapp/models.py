from django.db import models
from backweb.models import User


class Category(models.Model):
    c_name = models.CharField(max_length=16, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    f_type = models.ForeignKey('self', null=True)


    class Meta:
        db_table = 'category'



class Article(models.Model):

    title = models.CharField(max_length=31)
    a_content = models.TextField(null=True)
    a_keyword = models.CharField(max_length=64)
    a_describe = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    operate_time = models.DateTimeField(auto_now=True, null=True)
    c = models.ForeignKey(Category, null=True)
    u = models.ForeignKey(User, null=True)
    class Meta:
        db_table = 'article'