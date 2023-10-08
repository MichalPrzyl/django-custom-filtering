from rest_framework import serializers
# model
from article.models import Article
from author.models import Author
# serializers
from author.serializers import AuthorRelatedField

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorRelatedField(queryset=Author.objects.all())

    class Meta:
        model=Article
        fields = '__all__'
    

