from rest_framework import generics
# models
from article.models import Article
# serializers
from article.serializers import ArticleSerializer


class ArticleAPI(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
