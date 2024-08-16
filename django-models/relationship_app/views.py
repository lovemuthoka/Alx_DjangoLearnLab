from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import user_passes_test

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
    
    class CustomLoginView(LoginView):
    
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(CreateView):
    
    form_class= UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')