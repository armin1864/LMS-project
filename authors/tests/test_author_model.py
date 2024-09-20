import pytest
from authors.models import Authors


@pytest.mark.django_db
def test_create_book():
    author = Authors.objects.create(name="Test Author", bio="Test bio", nationality="Test Nationality")
    assert author.name == "Test Author"
    assert author.bio == "Test bio"
    assert author.nationality == "Test Nationality"
