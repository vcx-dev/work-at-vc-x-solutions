from .models import Author, Book
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        read_only_fields = ["id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            "id": representation["id"],
            "nome": representation["name"],
        }


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all(),
    )

    class Meta:
        model = Book
        fields = ["id", "name", "edition", "year_published", "authors"]
        read_only_fields = ["id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            "id": representation["id"],
            "nome": representation["name"],
            "edição": representation["edition"],
            "ano de publicação": representation["year_published"],
            "autores": representation["authors"],
        }
