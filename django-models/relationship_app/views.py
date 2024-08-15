from django.shortcuts import render
from .models import Book

def book_list_view(request):
    books = Book.objects.all()
    book_list = [(book.title, book.author) for book in books]
    return render(request, 'book_list.html', {'book_list': book_list})

from django.views.generic import ListView
from .models import Library, Book

class LibraryDetailView(ListView):
    model = Book
    template_name = 'library_detail.html'

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Book.objects.filter(library__id=library_id)

