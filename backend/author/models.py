from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    category = models.ForeignKey('author.AuthorCategory', models.SET_NULL, null=True)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)


class AuthorCategory(models.Model):
    name = models.CharField(max_length=255)
    tag = models.ForeignKey('author.Tag', models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
