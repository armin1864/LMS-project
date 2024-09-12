from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.serializers import BooksListSerializer
from books.models import Books


# these three functions are more restful but not good that much. go to bottom for the used function
'''
@api_view(['GET'])
def search_books_by_category(request, category):
    books = Books.objects.filter(category=category)
    if books:
        serializer = BooksListSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'no book with this category'})


@api_view(['GET'])
def search_books_by_author(request, author):
    books = Books.objects.filter(author=author)
    if books:
        serializer = BooksListSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'no book with this author'})
    
    
@api_view(['GET'])
def search_books_by_title(request, title):
    books = Books.objects.filter(title__icontains=title)
    if books:
        serializer = BooksListSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'no book with this title'})
'''


# this is a complete multiple search based on category and title and author
# how to use : /api/v1/search/?category=...&title=...&author=...
# note : you can use only wanted filters for example = /api/v1/search/?title=...
@api_view(['GET'])
def search_books(request):
    category = request.GET.get('category', default=None)
    author = request.GET.get('author', default=None)
    title = request.GET.get('title', default=None)

    books = Books.objects.all()
    if category:
        books = books.filter(category__iexact=category)
    if author:
        books = books.filter(author__iexact=author)
    if title:
        books = books.filter(title__icontains=title)

    if books.exists():
        serializer = BooksListSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'no book with this filter'})
