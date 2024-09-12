from rest_framework import serializers
from .models import Authors


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = [
            'id',
            'name',
            'bio',
            'nationality',
            'date_of_birth',
        ]


class AuthorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id', 'name',]
