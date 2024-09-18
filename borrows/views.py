from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BorrowTransactions
from books.models import Books
from reservations.models import Reservations


# receive a json with id and end_date and checks info and users number of borrow, if was ok adds a transaction
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_borrow_transaction(request):
    borrower = request.user
    if not borrower.total_borrows < 5:  # for number of borrows limit
        return Response({'error': 'borrow limit reached'})

    end_date = request.data.get('end_borrow_date')
    if not end_date:
        return Response({'error': 'no end borrow date received'})
    book_id = request.data.get('id')
    try:
        book = Books.objects.get(pk=book_id)
    except Books.DoesNotExist:
        return Response({'error': 'no book with this id'})
    if book.is_borrowed:
        return Response({'error': 'this book already borrowed'})
    if book.is_reserved:
        reserve_by_user = Reservations.objects.filter(reserver=borrower, book=book)
        if not reserve_by_user:
            return Response({'error': 'this book already reserved by other user'})

    transaction = BorrowTransactions(borrower=borrower, book=book, end_borrow_date=end_date)
    transaction.save()
    book.is_borrowed = True
    book.save()
    borrower.total_borrows += 1  # for number of borrows limit
    borrower.save()
    reserve_check = Reservations.objects.filter(reserver=borrower, book=book)  # check if user already reserved
    if reserve_check:  # if user reserved book then delete reserve
        reserve_check.delete()
    return Response('successful borrow')


# receive book id and check if this user borrowed this book or not. if yes,return date will add
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def return_borrow(request):
    borrower = request.user
    book_id = request.data.get('id')
    try:
        book = Books.objects.get(pk=book_id)
        borrow_transaction = BorrowTransactions.objects.get(book=book, borrower=borrower)
    except BorrowTransactions.DoesNotExist:
        return Response({'error': 'no such borrow found'})
    borrow_transaction.add_return_date()
    borrower.total_borrows -= 1  # for number of borrows limit
    borrower.save()
    return Response('successful return')
