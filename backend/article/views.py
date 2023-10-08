from rest_framework import generics
# models
from article.models import Article
# serializers
from article.serializers import ArticleSerializer
# filter
from django_filters.rest_framework import DjangoFilterBackend
from article.filters import MyFilterBackend


class ArticleAPI(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # filter_backends = [DjangoFilterBackend]
    filter_backends = [MyFilterBackend]
    # filterset_class = ArticleFilter
    filterset_fields = ['id', 'name']
