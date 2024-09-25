# Generated by Django 5.1.1 on 2024-09-23 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(related_name="books", to="api.author"),
        ),
        migrations.AlterField(
            model_name="book",
            name="edition",
            field=models.CharField(max_length=100, verbose_name="edição"),
        ),
        migrations.AlterField(
            model_name="book",
            name="name",
            field=models.CharField(max_length=100, verbose_name="nome"),
        ),
        migrations.AlterField(
            model_name="book",
            name="year_published",
            field=models.IntegerField(verbose_name="ano de publicação"),
        ),
    ]
