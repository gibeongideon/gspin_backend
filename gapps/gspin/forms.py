from django import forms
from .models import Account, Balance, Bet, AccountTopUp, BetResults, GameResult, BetTime, CustomUser


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_number', 'is_active', 'custom_user']


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['balance', 'account']


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['bet_amount', 'is_active', 'bet_choice', 'account', 'bet_time']


class AccountTopUpForm(forms.ModelForm):
    class Meta:
        model = AccountTopUp
        fields = ['topup_amount', 'account_to_topup']


class BetResultsForm(forms.ModelForm):
    class Meta:
        model = BetResults
        fields = ['name', 'bet_result']


class GameResultForm(forms.ModelForm):
    class Meta:
        model = GameResult
        fields = ['game_results', 'bet_time_result']


class BetTimeForm(forms.ModelForm):
    class Meta:
        model = BetTime
        fields = '__all__'


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'custom_user']


