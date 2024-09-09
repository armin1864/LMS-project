from django.db import models
from books.models import Books
from user_profile.models import User


class Reservations(models.Model):
    reserver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reserves')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reserves')
    reserve_date = models.DateField(auto_now_add=True)
