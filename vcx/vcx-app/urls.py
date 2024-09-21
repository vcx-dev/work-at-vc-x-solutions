"""
URL configuration for vcx-app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .api.views import (
    BooksView,
    AuthorsView,
    BookByIdView,
    AuthorBooksView,
    AuthorByIdView,
)
from django.views.decorators.csrf import get_token


urlpatterns = [
    path(
        "api/books/", BooksView.as_view(), name="all_books"
    ),  # usei esse as view por que fica mais clean e eh nativo do django
    path("api/authors/", AuthorsView.as_view(), name="all_authcors"),
    path("api/books/<int:id>/", BookByIdView.as_view(), name="book_by_id"),
    path("api/csrf-token/", get_token, name="api-csrf-token"),
    path("api/authors/<int:author_id>", AuthorBooksView.as_view()),
    path(
        "api/authors/<int:author_id>/books",
        AuthorBooksView.as_view(),
        name="author_books",
    ),
]
