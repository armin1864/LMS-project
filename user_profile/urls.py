from django.urls import path
from .views import UserProfileViewSet

urlpatterns = [
    path('', UserProfileViewSet.as_view({'get': 'user_profile'}), name='user_profile'),
    path('borrows/', UserProfileViewSet.as_view({'get': 'user_borrows'}), name='user_borrows'),
    path('reservations/', UserProfileViewSet.as_view({'get': 'user_reservations'}), name='user_reservations'),

]
