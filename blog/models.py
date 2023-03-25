from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    # define model for data base
    #this model has 3 item, title and body and author
    title = models.CharField(max_length= 50) # title limited by 50 character
    # foreignkey allows for many-to-one, that mean one user can be the author of several posts
    author = models.ForeignKey('auth.User' , on_delete=models.CASCADE) 
    body = models.TextField()

    #show title of post in preview of database
    def __str__(self):
        return self.title
    
    #how calculate the canonical url
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk' : self.pk})