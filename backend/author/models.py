from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
