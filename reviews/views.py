from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from borrows.models import BorrowTransactions
from .models import ReviewAndRatings
from .serializers import ReviewSerializer
from books.models import Books


# receive json with book id , review , rating and if borrow available with no review, add it
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_review(request):
    user = request.user
    book_id = request.data.get('id')
    review = request.data.get('review')
    rating = request.data.get('rating')

    try:  # for check if user borrowed this book or not
        book = Books.objects.get(pk=book_id)
        transaction = BorrowTransactions.objects.get(borrower=user, book=book)
    except BorrowTransactions.DoesNotExist:
        return Response({'error': 'this user doesnt borrow this book'})

    if ReviewAndRatings.objects.get(transaction=transaction):  # for check if user already reviewed or not
        return Response({'error': 'this user already reviewed this book'})

    new_review = ReviewAndRatings(transaction=transaction, review=review, rating=rating)
    new_review.save()
    return Response('successful review')


# sends reviews and ratings about selected book ( no permission needed )
@api_view(['GET'])
def see_reviews(request, pk):
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response({'error': 'no book with this id'})

    reviews = ReviewAndRatings.objects.filter(book=book)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
