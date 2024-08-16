from django.urls import path
from .views import list_books
from .views import  register, LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
 
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