from django.contrib import admin
from .models import Book  # Import your Book model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication year in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)