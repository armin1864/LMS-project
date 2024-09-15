from .models import BorrowTransactions
from rest_framework import serializers


# this serializer doesn't have borrower field and used for show requested user borrows
class BorrowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowTransactions
        fields = [
            'book',
            'borrow_date',
            'end_borrow_date',
            'return_date',
            'is_flagged',
        ]


class BorrowsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowTransactions
        fields = [
            'borrower',
            'book',
            'borrow_date',
            'end_borrow_date',
            'return_date',
            'is_flagged',
        ]
