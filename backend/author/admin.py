from django.contrib import admin

from .models import Author, AuthorCategory, Tag


admin.site.register(Author)
admin.site.register(AuthorCategory)
admin.site.register(Tag)

