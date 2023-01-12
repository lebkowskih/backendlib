from django.db import models

class BookModel(models.Model):
    title = models.CharField(max_length = 200)
    author = models.TextField()

    def __str__(self):
        return self.title
