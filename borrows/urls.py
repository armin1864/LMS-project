from django.urls import path
from .views import add_borrow_transaction, return_borrow

urlpatterns = [
    path('', add_borrow_transaction, name='add_borrow'),
    path('return/', return_borrow, name='return_borrow')
]
