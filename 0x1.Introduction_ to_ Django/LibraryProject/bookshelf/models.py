from django.db import models 

class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length= 100)
    publication_year = models. IntegerField()
     
def __str__(self):
        return self.title






