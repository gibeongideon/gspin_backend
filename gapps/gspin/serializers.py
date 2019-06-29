from . import models

from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = (
            'pk', 
            'account_number', 
            'created', 
            'last_updated', 
            'is_active', 
        )


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Balance
        fields = (
            'pk', 
            'balance', 
            'created', 
            'last_updated', 
        )


class BetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bet
        fields = (
            'pk', 
            'bet_amount', 
            'created', 
            'is_active', 
            'bet_choice', 
        )


class AccountTopUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AccountTopUp
        fields = (
            'pk', 
            'topup_amount', 
            'topup_time', 
        )


class BetResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BetResults
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class GameResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GameResult
        fields = (
            'pk', 
            'game_results', 
            'start_time', 
            'end_time', 
        )


class BetTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BetTime
        fields = (
            'pk', 
            'start_time', 
            'end_time', 
        )


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = (
            'pk', 
            'first_name', 
            'last_name', 
            'created', 
            'last_updated', 
        )


