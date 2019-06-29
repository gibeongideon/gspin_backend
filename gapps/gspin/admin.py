from django.contrib import admin
from django import forms
from .models import Account, Balance, Bet, AccountTopUp, BetResults, GameResult, BetTime, CustomUser

class AccountAdminForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = '__all__'


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    list_display = ['account_number', 'created', 'last_updated', 'is_active']
    readonly_fields = ['created', 'last_updated', 'is_active']

admin.site.register(Account, AccountAdmin)


class BalanceAdminForm(forms.ModelForm):

    class Meta:
        model = Balance
        fields = '__all__'


class BalanceAdmin(admin.ModelAdmin):
    form = BalanceAdminForm
    list_display = ['balance', 'created', 'last_updated']
    readonly_fields = ['balance', 'created', 'last_updated']

admin.site.register(Balance, BalanceAdmin)


class BetAdminForm(forms.ModelForm):

    class Meta:
        model = Bet
        fields = '__all__'


class BetAdmin(admin.ModelAdmin):
    form = BetAdminForm
    list_display = ['bet_amount', 'created', 'is_active', 'bet_choice']
    readonly_fields = ['bet_amount', 'created', 'is_active', 'bet_choice']

admin.site.register(Bet, BetAdmin)


class AccountTopUpAdminForm(forms.ModelForm):

    class Meta:
        model = AccountTopUp
        fields = '__all__'


class AccountTopUpAdmin(admin.ModelAdmin):
    form = AccountTopUpAdminForm
    list_display = ['topup_amount', 'topup_time']
    readonly_fields = ['topup_amount', 'topup_time']

admin.site.register(AccountTopUp, AccountTopUpAdmin)


class BetResultsAdminForm(forms.ModelForm):

    class Meta:
        model = BetResults
        fields = '__all__'


class BetResultsAdmin(admin.ModelAdmin):
    form = BetResultsAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(BetResults, BetResultsAdmin)


class GameResultAdminForm(forms.ModelForm):

    class Meta:
        model = GameResult
        fields = '__all__'


class GameResultAdmin(admin.ModelAdmin):
    form = GameResultAdminForm
    list_display = ['game_results', 'start_time', 'end_time']
    readonly_fields = ['game_results', 'start_time', 'end_time']

admin.site.register(GameResult, GameResultAdmin)


class BetTimeAdminForm(forms.ModelForm):

    class Meta:
        model = BetTime
        fields = '__all__'


class BetTimeAdmin(admin.ModelAdmin):
    form = BetTimeAdminForm
    list_display = ['start_time', 'end_time']
    readonly_fields = ['start_time', 'end_time']

admin.site.register(BetTime, BetTimeAdmin)


class CustomUserAdminForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm
    list_display = ['first_name', 'last_name', 'created', 'last_updated']
    readonly_fields = ['first_name', 'last_name', 'created', 'last_updated']

admin.site.register(CustomUser, CustomUserAdmin)


