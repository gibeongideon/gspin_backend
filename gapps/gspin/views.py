from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Account, Balance, Bet, AccountTopUp, BetResults, GameResult, BetTime, CustomUser
from .forms import AccountForm, BalanceForm, BetForm, AccountTopUpForm, BetResultsForm, GameResultForm, BetTimeForm, CustomUserForm


class AccountListView(ListView):
    model = Account


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm


class AccountDetailView(DetailView):
    model = Account


class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm


class BalanceListView(ListView):
    model = Balance


class BalanceCreateView(CreateView):
    model = Balance
    form_class = BalanceForm


class BalanceDetailView(DetailView):
    model = Balance


class BalanceUpdateView(UpdateView):
    model = Balance
    form_class = BalanceForm


class BetListView(ListView):
    model = Bet


class BetCreateView(CreateView):
    model = Bet
    form_class = BetForm


class BetDetailView(DetailView):
    model = Bet


class BetUpdateView(UpdateView):
    model = Bet
    form_class = BetForm


class AccountTopUpListView(ListView):
    model = AccountTopUp


class AccountTopUpCreateView(CreateView):
    model = AccountTopUp
    form_class = AccountTopUpForm


class AccountTopUpDetailView(DetailView):
    model = AccountTopUp


class AccountTopUpUpdateView(UpdateView):
    model = AccountTopUp
    form_class = AccountTopUpForm


class BetResultsListView(ListView):
    model = BetResults


class BetResultsCreateView(CreateView):
    model = BetResults
    form_class = BetResultsForm


class BetResultsDetailView(DetailView):
    model = BetResults


class BetResultsUpdateView(UpdateView):
    model = BetResults
    form_class = BetResultsForm


class GameResultListView(ListView):
    model = GameResult


class GameResultCreateView(CreateView):
    model = GameResult
    form_class = GameResultForm


class GameResultDetailView(DetailView):
    model = GameResult


class GameResultUpdateView(UpdateView):
    model = GameResult
    form_class = GameResultForm


class BetTimeListView(ListView):
    model = BetTime


class BetTimeCreateView(CreateView):
    model = BetTime
    form_class = BetTimeForm


class BetTimeDetailView(DetailView):
    model = BetTime


class BetTimeUpdateView(UpdateView):
    model = BetTime
    form_class = BetTimeForm


class CustomUserListView(ListView):
    model = CustomUser


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm


class CustomUserDetailView(DetailView):
    model = CustomUser


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm

