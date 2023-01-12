from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookModel

class BooksViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
