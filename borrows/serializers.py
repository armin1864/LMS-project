from .models import BorrowTransactions
from rest_framework import serializers


class BorrowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowTransactions
        fields = [
            'book',
            'borrow_date',
            'return_date',
            'is_flagged',
        ]
