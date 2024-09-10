from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BooksSerializer, BooksListSerializer
from .models import Books


# show books list : all -> all books in library , available -> just available books for reserve
@api_view(['GET'])
def books_list(request, filter):
    if filter == 'all':
        books = Books.objects.all()
    elif filter == 'available':
        books = Books.objects.filter(is_borrowed=False, is_reserved=False)
    else:
        return Response({'error': 'use valid filter'})
    serializer = BooksListSerializer(books, many=True)
    return Response(serializer.data)


# shows all details about selected book
@api_view(['get'])
def book_details(request, pk):
    try:
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    except Books.DoesNotExist:
        return Response({'error': 'no book with this id'})
