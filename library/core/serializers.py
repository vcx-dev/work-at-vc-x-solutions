from rest_framework import serializers
from .models import book, author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ["id", "name", "edition", "publication_year", "authors"]
