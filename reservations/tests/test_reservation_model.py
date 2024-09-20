import pytest
from user_profile.models import User
from reservations.models import Reservations
from test_reservation_views import create_test_book


@pytest.mark.django_db
def test_reserve():
    reserver = User.objects.create(username='test username', password='test', email='test@test.com')
    book = create_test_book()
    reserve = Reservations.objects.create(reserver=reserver, book=book)
    assert reserve.book.title == "Test Book"
    assert reserve.reserver.username == 'test username'


