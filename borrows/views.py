from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BorrowTransactions
from books.models import Books


# receive a json with id and end_date and checks info and users number of borrow, if was ok adds a transaction
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_borrow_transaction(request):

    borrower = request.user
    total_reserve = borrower.total_reserves
    if not total_reserve < 5:  # for number of borrows limit
        return Response({'error': 'borrow limit reached'})

    end_date = request.data.get('end_borrow_date')
    if not end_date:
        return Response({'error': 'no end borrow date received'})
    book_id = request.data.get('id')
    try:
        book = Books.objects.get(pk=book_id)
    except Books.DoesNotExist:
        return Response({'error': 'no book with this id'})
    if book.is_borrowed or book.is_reserved:
        return Response({'error': 'this book already borrowed or reserved'})

    transaction = BorrowTransactions(borrower=borrower, book=book, end_borrow_date=end_date)
    transaction.save()
    book.is_borrowed = True
    book.save()
    borrower.total_reserves += 1  # for number of borrows limit
    borrower.save()
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
    borrower.total_reserves -= 1  # for number of borrows limit
    borrower.save()
