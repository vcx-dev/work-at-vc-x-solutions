from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Author, Book
from api.serializer import AuthorSerializer
import json


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Author Name")
        self.author2 = Author.objects.create(name="second author")
        self.book_data = {
            "nome": "New Book",
            "edição": "Second Edition",
            "ano de publicação": 2022,
            "autores": [self.author.id],
        }
        self.book = Book.objects.create(
            name="Existing Book", edition="First", year_published=2021
        )
        self.book.authors.add(self.author)

    def test_get_books(self):
        response = self.client.get(reverse("all_books"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        response = self.client.post(reverse("all_books"), self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_author(self):
        data = {"nome": "Test"}

        # Serialize the data
        serializer = AuthorSerializer(data=data)

        # Validate the serializer
        if serializer.is_valid():
            # Get the serialized data
            serialized_data = serializer.data

            # Use the client to send a POST request with serialized data
            response = self.client.post(
                reverse("authors"),
                serialized_data,
                format="json",  # Ensure that data is sent as JSON
            )

            # Check if the response is created successfully
            assert response.status_code == status.HTTP_201_CREATED

            # Optionally, verify the content of the response
            created_author = Author.objects.get(name="Test")
            assert response.data["name"] == created_author.name

    def test_search_author_by_name(self):
        other_author = Author.objects.create(name="Another Author")
        # Perform the GET request
        response = self.client.get(reverse("authors") + f"?nome={self.author.name}")
        assert response.status_code == 200
        authors = response.json()
        assert len(authors) == 1
        assert authors[0]["nome"] == self.author.name

    def test_delete_author_only_book(self):
        author_id = self.author.id
        # print(author_id)
        url = reverse("author_id", args=[author_id])
        # print(url)
        response = self.client.delete(url)
        # print(response.status_code)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    # como tem 2 autores, vou conseguir deletar, pro livro nao ficar sem autor.
    def test_delete_author(self):
        self.book.authors.add(self.author2)
        response = self.client.delete(reverse("author_id", args=[self.author.id]))
        assert response.status_code == status.HTTP_200_OK

    def test_update_book(self):
        updated_data = {
            "nome": "Updated Book",
            "edição": "Updated Edition",
            "ano de publicação": 2023,
            "autores": [self.author.id],
        }
        response = self.client.put(
            reverse("book_by_id", kwargs={"id": self.book.id}),
            updated_data,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)  # Decode JSON response
        self.assertEqual(response_data["nome"], "Updated Book")

    def test_delete_book_by_id(self):
        response = self.client.delete(
            reverse("book_by_id", kwargs={"id": self.book.id})
        )
        assert response.status_code == status.HTTP_200_OK

    def test_filter_books(self):
        # Create some authors
        author1 = Author.objects.create(name="Author One")
        author2 = Author.objects.create(name="Author Two")

        # Create some books
        self.book1 = Book.objects.create(
            name="Book One", edition="First", year_published=2021
        )
        self.book1.authors.add(author1)

        self.book2 = Book.objects.create(
            name="Book Two", edition="Second", year_published=2022
        )
        self.book2.authors.add(author2)

        self.book3 = Book.objects.create(
            name="Another Book", edition="First", year_published=2021
        )
        self.book3.authors.add(author1, author2)

        # Test filtering by name
        response = self.client.get(reverse("all_books"), {"nome": "Book One"})
        print(response.content)
        assert response.status_code == 200
        books = response.json()
        assert len(books) == 1
        assert books[0]["nome"] == self.book1.name  # Ensure using self.book1

        # Test filtering by edition
        response = self.client.get(reverse("all_books"), {"edição": self.book1.edition})
        assert response.status_code == 200
        books = response.json()
        print(books)
        assert len(books) == 3  # Both book1 and book3 have "First" edition

        # Test filtering by year published
        response = self.client.get(reverse("all_books"), {"ano de publicação": 2021})
        assert response.status_code == 200
        books = response.json()
        assert len(books) == 3  # Both book1 and book3 were published in 2021

        # Test filtering by authors (using the author's ID)
        response = self.client.get(reverse("all_books"), {"autores": author1.id})
        assert response.status_code == 200
        books = response.json()
        assert len(books) == 2  # All three books include author1

    def test_delete_book(self):
        response = self.client.delete(
            reverse("book_by_id", kwargs={"id": self.book.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
