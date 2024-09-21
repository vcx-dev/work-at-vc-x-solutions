from .models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ["id"]


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all(),  # trata os autores com pk e nao objetos
    )

    class Meta:
        model = Book
        fields = ["id", "name", "edition", "year_published", "authors"]
        read_only_fields = ["id"]
