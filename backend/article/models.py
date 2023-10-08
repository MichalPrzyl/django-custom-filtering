from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('author.Author', models.DO_NOTHING)
    created_dt = models.DateField()
