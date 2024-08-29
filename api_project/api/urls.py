from api.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),  # Include API app URLs
]

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]