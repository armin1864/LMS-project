from django.urls import path
from .views import books_list, book_details


urlpatterns = [
    path('<str:filter>/', books_list, name='books_list'),
    path('detail/<int:pk>/', book_details, name='book_details')
]