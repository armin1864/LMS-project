from rest_framework import serializers
from .models import ReviewAndRatings


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAndRatings
        fields = [
            'transaction',
            'review',
            'rating',
        ]
