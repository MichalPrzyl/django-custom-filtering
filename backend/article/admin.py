from django.contrib import admin


from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']

admin.site.register(Article, ArticleAdmin)