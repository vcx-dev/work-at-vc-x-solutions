from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    edition = models.CharField(max_length=100)
    year_published = models.IntegerField()
    authors = models.ManyToManyField(Author) #django ja relaciona automaticamente para mim

