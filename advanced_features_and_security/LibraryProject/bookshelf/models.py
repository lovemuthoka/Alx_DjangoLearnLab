from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .models import CustomUser

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length= 100)
    publication_year = models. IntegerField()
     
def __str__(self):
        return self.title




class CustomUserManager(models.Manager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    class SomeModel(models.Model):
      user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)