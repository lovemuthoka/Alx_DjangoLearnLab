from django.urls import path
from .views import list_books

urlpatterns = [
    # URL pattern for the function-based view that lists all books
    path('books/', book_list_view, name='book-list'),

    # URL pattern for the class-based view that displays details for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
