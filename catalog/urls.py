from django.urls import path, re_path

from catalog.views import index, AuthorListView, AuthorDetailView, BooksListView, BooksDetailView

urlpatterns = [
    path('', index, name='index'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('books/', BooksListView.as_view(), name='books'),

    re_path(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^books/(?P<pk>\d+)', BooksDetailView.as_view(), name='book-detail')
]
