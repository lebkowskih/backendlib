from rest_framework import serializers

from .models import BookModel

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Book:
        model = BookModel
        fields = ('title', 'author')