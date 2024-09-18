from celery import shared_task
from borrows.models import BorrowTransactions
from django.db.models import Count


@shared_task
def make_report():
    transactions = BorrowTransactions.objects.all()
    overdue = []
    for transaction in transactions:
        if transaction.is_flagged:
            overdue.append(transaction)

    most_borrowed = BorrowTransactions.objects.values('book').annotate(book_count=Count(
        'book')).order_by('-book_count').first()

    report = {
        'overdue': overdue,
        'most_borrowed': most_borrowed,
    }
    return report
