from rest_framework import serializers
# model
from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields = '__all__'
    

