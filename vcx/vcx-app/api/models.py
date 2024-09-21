from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="nome")
    edition = models.CharField(max_length=100, verbose_name="edição")
    year_published = models.IntegerField(max_length=5, verbose_name="ano de publicação")
    authors = models.ManyToManyField(
        Author, related_name="books"
    )  # django ja relaciona automaticamente, nome eh books
