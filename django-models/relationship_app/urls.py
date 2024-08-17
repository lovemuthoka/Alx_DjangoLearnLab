from django.urls import path
from .views import list_books
from .views import  register, LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .views import admin_view, librarian_view, member_view
from . import views

urlpatterns = [
    # URL pattern for the function-based view that lists all books
    path('books/', book_list_view, name='book-list'),

    # URL pattern for the class-based view that displays details for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
   
]

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
]

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    # Other URL patterns...
]
urlpatterns = [
     # Other URL patterns...

    # URL pattern for adding a book
    path('add/', views.add_book, name='add_book'),

    # URL pattern for editing a book
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),

    # URL pattern for deleting a book
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
