from django.contrib import admin

from .models import Author, AuthorCategory


admin.site.register(Author)
admin.site.register(AuthorCategory)

