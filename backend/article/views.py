from rest_framework import generics
# models
from article.models import Article
# serializers
from article.serializers import ArticleSerializer
# filter
from django_filters.rest_framework import DjangoFilterBackend


class ArticleAPI(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
