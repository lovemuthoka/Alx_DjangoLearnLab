from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library  # Ensure both Book and Library models are imported

# Function-based view to list all books
def book_list_view(request):
    books = Book.objects.all()  # Retrieve all books from the database
    book_list = [(book.title, book.author.name) for book in books]  # Create a list of tuples with book titles and authors
    return render(request, 'relationship_app/list_books.html', {'book_list': book_list})  # Render the list_books.html template

# Class-based view to display details for a specific library
class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'  # Use the library_detail.html template for this view
    context_object_name = 'books'  # Context variable name to be used in the template

    def get_queryset(self):
        library_id = self.kwargs['library_id']  # Retrieve the library_id from the URL
        return Book.objects.filter(library__id=library_id)  # Filter books by the specified library
