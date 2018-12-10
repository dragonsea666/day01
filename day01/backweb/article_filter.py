


from rest_framework import filters
import django_filters
from myapp.models import Article
class ArticleFilter(filters.FilterSet):
    # 过滤URL中的title参数
    title = django_filters.CharFilter('title', lookup_expr='contains')
    desc = django_filters.CharFilter('a_describe', lookup_expr='contains')
    content = django_filters.CharFilter('a_content', lookup_expr='contains')
    keyword = django_filters.CharFilter('a_keyword', lookup_expr='contains')
    # 过滤URL中时间最小值的min_time
    min_time = django_filters.DateTimeFilter('create_time', lookup_expr='gt')
    max_time = django_filters.DateTimeFilter('create_time', lookup_expr='lt')
    class Meta:
        model = Article
        fields = ['title','desc','content','keyword','min_time','max_time']


