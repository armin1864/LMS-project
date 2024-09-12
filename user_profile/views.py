from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from borrows.serializers import BorrowsSerializer
from borrows.models import BorrowTransactions
from reservations.models import Reservations
from reservations.serializers import ReservationSerializer


class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='')
    def user_profile(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='borrows')
    def user_borrows(self, request):
        user = request.user
        borrows = BorrowTransactions.objects.filter(borrower=user)
        serializer = BorrowsSerializer(borrows, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='reservations')
    def user_reservations(self, request):
        user = request.user
        reserves = Reservations.objects.filter(reserver=user)
        serializer = ReservationSerializer(reserves, many=True)
        return Response(serializer.data)
