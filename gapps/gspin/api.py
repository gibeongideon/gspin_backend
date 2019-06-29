from . import models
from . import serializers
from rest_framework import viewsets, permissions


class AccountViewSet(viewsets.ModelViewSet):
    """ViewSet for the Account class"""

    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class BalanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Balance class"""

    queryset = models.Balance.objects.all()
    serializer_class = serializers.BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class BetViewSet(viewsets.ModelViewSet):
    """ViewSet for the Bet class"""

    queryset = models.Bet.objects.all()
    serializer_class = serializers.BetSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountTopUpViewSet(viewsets.ModelViewSet):
    """ViewSet for the AccountTopUp class"""

    queryset = models.AccountTopUp.objects.all()
    serializer_class = serializers.AccountTopUpSerializer
    permission_classes = [permissions.IsAuthenticated]


class BetResultsViewSet(viewsets.ModelViewSet):
    """ViewSet for the BetResults class"""

    queryset = models.BetResults.objects.all()
    serializer_class = serializers.BetResultsSerializer
    permission_classes = [permissions.IsAuthenticated]


class GameResultViewSet(viewsets.ModelViewSet):
    """ViewSet for the GameResult class"""

    queryset = models.GameResult.objects.all()
    serializer_class = serializers.GameResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class BetTimeViewSet(viewsets.ModelViewSet):
    """ViewSet for the BetTime class"""

    queryset = models.BetTime.objects.all()
    serializer_class = serializers.BetTimeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
    """ViewSet for the CustomUser class"""

    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


