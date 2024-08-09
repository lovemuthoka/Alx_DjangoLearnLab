from django.contrib import admin
from .models import Book  # Import your Book model

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)
