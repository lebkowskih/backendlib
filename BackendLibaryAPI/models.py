from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    nationality = models.CharField(max_length=100)
    author_description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_description = models.TextField()
    

class Book(models.Model):
    title = models.CharField(max_length = 200)
    isbn = models.IntegerField(max_length=13)
    date_of_publication = models.DateField()
    quantity = models.IntegerField()
    book_description = models.TextField()
    language = models.TextField()
    author_id = models.ManyToManyField(Author)
    category_id = models.ManyToManyField(Category)

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    username = None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []