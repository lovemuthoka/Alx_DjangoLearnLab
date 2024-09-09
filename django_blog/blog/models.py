from django.db import models
from django.contrib.auth.models import User  # Import Django's User model
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author=  models.ForeignKey(User,on_delete=models.CASCADE related_name="Post")
    def __str__(self):
        return self.title
    
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship with Tag

    def __str__(self):
        return self.title
