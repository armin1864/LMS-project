from rest_framework import serializers
from .models import Books


# just listing important details from books for main page
class BooksListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'author']


# listing all details about books for details page
class BooksSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'description', 'author', 'isbn', 'category', 'publication_date', 'is_borrowed',
                  'is_reserved']
