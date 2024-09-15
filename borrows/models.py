from django.db import models
from books.models import Books
from user_profile.models import User
from datetime import date


class BorrowTransactions(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField(auto_now_add=True)
    end_borrow_date = models.DateField(default=date.today())
    return_date = models.DateField(blank=True, null=True)
    is_flagged = models.BooleanField(default=False)

    def add_return_date(self):
        self.return_date = date.today()
        self.book.is_borrowed = False
        self.book.save()
        self.save()

    def check_flag(self):
        if not self.return_date:
            if date.today() > self.end_borrow_date:
                self.is_flagged = True
                self.save()
        return self.is_flagged
