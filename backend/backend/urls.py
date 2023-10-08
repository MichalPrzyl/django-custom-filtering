from django.contrib import admin
from django.urls import path
# views
from article.views import ArticleAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles', ArticleAPI.as_view()),
]
