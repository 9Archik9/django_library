from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_book_instance = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='Available').count()

    return render(request, "index.html", {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_book_instance': num_book_instance,
        'num_instances_available': num_instances_available,
    })


class AuthorListView(ListView):
    model = Author
    template_name = "authors_list.html"
    context_object_name = "authors_list"


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors_detail.html'


class BooksListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books_list"


class BooksDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookInstanceDetailView(ListView):
    model = BookInstance
    template_name = "book_instance.html"
