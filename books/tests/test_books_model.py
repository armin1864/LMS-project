import pytest
from books.models import Books
from authors.models import Authors


@pytest.mark.django_db
def test_create_book():
    author = Authors.objects.create(name="Test Author")
    book = Books.objects.create(title="Test Book", author=author, description="Test description",
                                isbn="Test ISBN", category="Test Category")
    assert book.title == "Test Book"
    assert book.author.name == "Test Author"
    assert book.description == "Test description"
    assert book.isbn == "Test ISBN"
    assert book.category == "Test Category"
