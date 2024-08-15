from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list_view, name='book_list'),
    path('library/<int:library_id>/', views.LibraryDetailView.as_view(), name='library_detail'),
]