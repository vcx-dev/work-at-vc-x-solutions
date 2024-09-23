from .models import Author, Book
from rest_framework import serializers
from datetime import datetime


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

    def validate_year_published(self, value):
        current_year = datetime.now().year
        if value < -3000 or value > current_year:
            raise serializers.ValidationError(
                f"Year must be between -5000 and {current_year}.", "404"
            )
        return value
