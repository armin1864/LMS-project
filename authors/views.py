from .serializers import AuthorsSerializer, AuthorsListSerializer
from .models import Authors
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Books
from books.serializers import BooksListSerializer


# show all authors
@api_view(['GET'])
def authors_list(request):
    authors = Authors.objects.all()
    if authors:
        serializer = AuthorsListSerializer(authors, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'this author doesnt have book'})


# show selected author bio
@api_view(['GET'])
def author_bio(request, pk):
    try:
        authors = Authors.objects.get(pk=pk)
        serializer = AuthorsSerializer(authors)
        return Response(serializer.data)
    except Authors.DoesNotExist:
        return Response({'error': 'no author with this id'})


# show selected author books
@api_view(['GET'])
def author_books(request, pk):
    books = Books.objects.filter(author_id=pk)
    if books:
        serializer = BooksListSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'this author doesnt have book'})
