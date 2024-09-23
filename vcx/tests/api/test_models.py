from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Book, Author


class ModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            name="Book Title", edition="First Edition", year_published=2021
        )
        self.book.authors.add(self.author)

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Author Name")

    def test_book_creation(self):
        self.assertEqual(self.book.name, "Book Title")
        self.assertEqual(self.book.edition, "First Edition")
        self.assertEqual(self.book.year_published, 2021)
        self.assertIn(self.author, self.book.authors.all())

    def test_book_author_relation(self):
        self.assertEqual(self.book.authors.all()[0].name, "Author Name")


class AuthorDeletionTest(TestCase):

    def setUp(self):
        # Create an author and a book
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            name="Test Book", edition="First", year_published=2020
        )
        self.book.authors.add(self.author)

    def test_delete_author(self):

        self.assertEqual(self.book.authors.count(), 1)

        self.author.delete()

        self.assertEqual(self.book.authors.count(), 1)  # fiz um metodo de protecao
