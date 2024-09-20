import pytest
from books.models import Books
from user_profile.models import User
from borrows.models import BorrowTransactions
from authors.models import Authors


@pytest.mark.django_db
def test_borrow():
    borrower = User.objects.create(username='test username', password='test', email='test@test.com')
    author = Authors.objects.create(name="Test Author")
    book = Books.objects.create(title="Test Book", author=author, description="Test description",
                                isbn="Test ISBN", category="Test Category")
    borrow = BorrowTransactions.objects.create(borrower=borrower, book=book)

    assert borrow.book.title == "Test Book"
    assert borrow.borrower.email == "test@test.com"
