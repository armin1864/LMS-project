from celery import shared_task
from .models import BorrowTransactions
from datetime import date
from django.core.mail import send_mail


# checks if book not returned and if end date passed, flags transaction
@shared_task
def check_and_flag():
    borrows = BorrowTransactions.objects.all()
    for borrow in borrows:
        if not borrow.return_date:  # checks if book already returned, pass this transaction
            if date.today() > borrow.end_borrow_date:
                borrow.is_flagged = True
                borrow.save()
    return BorrowTransactions.objects.filter(is_flagged=True)


@shared_task
def notify_overdue():
    borrows = BorrowTransactions.objects.filter(is_flagged=True)
    for borrow in borrows:
        message = f"end time of your borrow for book {borrow.book.title} already past. please return book "
        send_mail(
            'Notification',
            message,
            'abc@abc.com',
            borrow.borrower.email,
            fail_silently=False,
        )
        