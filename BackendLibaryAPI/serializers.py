from rest_framework import serializers

from .models import Book,Author,Category

class BookSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id','title','isbn','date_of_publication','quantity','book_description','author_id','category_id')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
     
    class Meta:
        model = Author
        fields = ('id','name', 'surname','birthday','nationality','author_description')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
     
    class Meta:
        model = Category
        fields = ('id','name', 'category_description')
    