from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksViewSet, AuthorsViewSet, BorrowsViewSet, UsersViewSet, ReservationsViewSet, ReviewsViewSet

router = DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'authors', AuthorsViewSet)
router.register(r'borrows', BorrowsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'reservations', ReservationsViewSet)
router.register(r'reviews', ReviewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
