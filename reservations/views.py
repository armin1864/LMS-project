from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from books.models import Books
from .models import Reservations


# receive a json with book id in body and auth token in header, checks if ok and then save the reservation
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_reservation(request):

    reserver = request.user
    book_id = request.data.get('id')
    try:
        book = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        return Response({'error': 'no book with this id'})
    if book.is_reserved:
        return Response({'error': 'this book already reserved'})
    if not book.is_borrowed:
        return Response({'error': 'this book already available for borrow'})

    reservation = Reservations(reserver=reserver, book=book)
    reservation.save()
    book.is_reserved = True
    book.save()
    return Response('successful reservation')
