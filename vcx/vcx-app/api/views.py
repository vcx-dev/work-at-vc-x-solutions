# views.py
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book, Author
from .serializer import BookSerializer, AuthorSerializer
import json


# Class-based view for listing and creating books
class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(
            serializer.data, safe=False
        )  # Safe=False allows a list to be returned

    def post(self, request):
        try:
            # Load the data from request.body
            data = json.loads(request.body)
            # Serialize the data
            serializer = BookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


# Class-based view for retrieving a book by its ID
class BookByIdView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        book = get_object_or_404(Book, id=id)
        data = json.loads(request.body)
        serializer = BookSerializer(book, data=data)  # atualizando o atual
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        book = get_object_or_404(Book, id=id)
        book.delete()


# Class-based view for listing and creating authors
class AuthorsView(View):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():  # se tiver todos os campos no formato correto
            serializer.save()  # salva
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# classe para retornar todos os livros feitos por um author
class AuthorBooksView(View):
    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)  # try catch basicamente
        books_made_by_author = author.books.all()
        serializer = BookSerializer(books_made_by_author, many=True)
        return JsonResponse(serializer.data, safe=False)


class AuthorByIdView(View):
    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)
