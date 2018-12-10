from rest_framework import serializers
from myapp.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'a_describe', 'a_content', 'id', 'a_keyword', 'operate_time', 'create_time', 'c']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.c:
            data['c'] = instance.c.c_name
        return data


