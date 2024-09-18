from celery import shared_task
from .models import Reservations
from django.core.mail import send_mail


# this method notify users when their reserve become available for borrow
@shared_task
def notify_reservation():
    reserves = Reservations.objects.filter(book__is_borrowed=False)
    for reserve in reserves:
        message = f"your reservation for book {reserve.book.title} is now available for borrow"
        send_mail(
            'Notification',
            message,
            'abc@abc.com',
            reserve.reserver.email,
            fail_silently=False,
        )
