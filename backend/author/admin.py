from django.contrib import admin

from .models import Author, AuthorCategory, Tag


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorCategory)
admin.site.register(Tag)

