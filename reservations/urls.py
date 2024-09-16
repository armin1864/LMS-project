from django.urls import path
from .views import add_reservation


urlpatterns = [
    path('', add_reservation, name='add_reservation')
]
