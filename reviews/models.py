from django.db import models
from borrows.models import BorrowTransactions
from books.models import Books


class ReviewAndRatings(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    transaction = models.OneToOneField(BorrowTransactions, on_delete=models.CASCADE)
    review = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField()
