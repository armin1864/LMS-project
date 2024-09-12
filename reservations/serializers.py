from .models import Reservations
from rest_framework import serializers


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = [
            'book',
            'reserve_date',
        ]
