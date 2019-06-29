import unittest
from django.urls import reverse
from django.test import Client
from .models import Account, Balance, Bet, AccountTopUp, BetResults, GameResult, BetTime, CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_account(**kwargs):
    defaults = {}
    defaults["account_number"] = "account_number"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "custom_user" not in defaults:
        defaults["custom_user"] = create_customuser()
    return Account.objects.create(**defaults)


def create_balance(**kwargs):
    defaults = {}
    defaults["balance"] = "balance"
    defaults.update(**kwargs)
    if "account" not in defaults:
        defaults["account"] = create_account()
    return Balance.objects.create(**defaults)


def create_bet(**kwargs):
    defaults = {}
    defaults["bet_amount"] = "bet_amount"
    defaults["is_active"] = "is_active"
    defaults["bet_choice"] = "bet_choice"
    defaults.update(**kwargs)
    if "account" not in defaults:
        defaults["account"] = create_account()
    if "bet_time" not in defaults:
        defaults["bet_time"] = create_bettime()
    return Bet.objects.create(**defaults)


def create_accounttopup(**kwargs):
    defaults = {}
    defaults["topup_amount"] = "topup_amount"
    defaults.update(**kwargs)
    if "account_to_topup" not in defaults:
        defaults["account_to_topup"] = create_account()
    return AccountTopUp.objects.create(**defaults)


def create_betresults(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "bet_result" not in defaults:
        defaults["bet_result"] = create_bet()
    return BetResults.objects.create(**defaults)


def create_gameresult(**kwargs):
    defaults = {}
    defaults["game_results"] = "game_results"
    defaults.update(**kwargs)
    if "bet_time_result" not in defaults:
        defaults["bet_time_result"] = create_bettime()
    return GameResult.objects.create(**defaults)


def create_bettime(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return BetTime.objects.create(**defaults)


def create_customuser(**kwargs):
    defaults = {}
    defaults["first_name"] = "first_name"
    defaults["last_name"] = "last_name"
    defaults.update(**kwargs)
    if "custom_user" not in defaults:
        defaults["custom_user"] = create_django_contrib_auth_models_user()
    return CustomUser.objects.create(**defaults)


class AccountViewTest(unittest.TestCase):
    '''
    Tests for Account
    '''
    def setUp(self):
        self.client = Client()

    def test_list_account(self):
        url = reverse('gspin_account_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_account(self):
        url = reverse('gspin_account_create')
        data = {
            "account_number": "account_number",
            "is_active": "is_active",
            "custom_user": create_customuser().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_account(self):
        account = create_account()
        url = reverse('gspin_account_detail', args=[account.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        account = create_account()
        data = {
            "account_number": "account_number",
            "is_active": "is_active",
            "custom_user": create_customuser().pk,
        }
        url = reverse('gspin_account_update', args=[account.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BalanceViewTest(unittest.TestCase):
    '''
    Tests for Balance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_balance(self):
        url = reverse('gspin_balance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_balance(self):
        url = reverse('gspin_balance_create')
        data = {
            "balance": "balance",
            "account": create_account().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_balance(self):
        balance = create_balance()
        url = reverse('gspin_balance_detail', args=[balance.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_balance(self):
        balance = create_balance()
        data = {
            "balance": "balance",
            "account": create_account().pk,
        }
        url = reverse('gspin_balance_update', args=[balance.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BetViewTest(unittest.TestCase):
    '''
    Tests for Bet
    '''
    def setUp(self):
        self.client = Client()

    def test_list_bet(self):
        url = reverse('gspin_bet_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bet(self):
        url = reverse('gspin_bet_create')
        data = {
            "bet_amount": "bet_amount",
            "is_active": "is_active",
            "bet_choice": "bet_choice",
            "account": create_account().pk,
            "bet_time": create_bettime().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bet(self):
        bet = create_bet()
        url = reverse('gspin_bet_detail', args=[bet.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bet(self):
        bet = create_bet()
        data = {
            "bet_amount": "bet_amount",
            "is_active": "is_active",
            "bet_choice": "bet_choice",
            "account": create_account().pk,
            "bet_time": create_bettime().pk,
        }
        url = reverse('gspin_bet_update', args=[bet.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AccountTopUpViewTest(unittest.TestCase):
    '''
    Tests for AccountTopUp
    '''
    def setUp(self):
        self.client = Client()

    def test_list_accounttopup(self):
        url = reverse('gspin_accounttopup_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_accounttopup(self):
        url = reverse('gspin_accounttopup_create')
        data = {
            "topup_amount": "topup_amount",
            "account_to_topup": create_account().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_accounttopup(self):
        accounttopup = create_accounttopup()
        url = reverse('gspin_accounttopup_detail', args=[accounttopup.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_accounttopup(self):
        accounttopup = create_accounttopup()
        data = {
            "topup_amount": "topup_amount",
            "account_to_topup": create_account().pk,
        }
        url = reverse('gspin_accounttopup_update', args=[accounttopup.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BetResultsViewTest(unittest.TestCase):
    '''
    Tests for BetResults
    '''
    def setUp(self):
        self.client = Client()

    def test_list_betresults(self):
        url = reverse('gspin_betresults_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_betresults(self):
        url = reverse('gspin_betresults_create')
        data = {
            "name": "name",
            "bet_result": create_bet().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_betresults(self):
        betresults = create_betresults()
        url = reverse('gspin_betresults_detail', args=[betresults.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_betresults(self):
        betresults = create_betresults()
        data = {
            "name": "name",
            "bet_result": create_bet().pk,
        }
        url = reverse('gspin_betresults_update', args=[betresults.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class GameResultViewTest(unittest.TestCase):
    '''
    Tests for GameResult
    '''
    def setUp(self):
        self.client = Client()

    def test_list_gameresult(self):
        url = reverse('gspin_gameresult_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_gameresult(self):
        url = reverse('gspin_gameresult_create')
        data = {
            "game_results": "game_results",
            "bet_time_result": create_bettime().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_gameresult(self):
        gameresult = create_gameresult()
        url = reverse('gspin_gameresult_detail', args=[gameresult.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_gameresult(self):
        gameresult = create_gameresult()
        data = {
            "game_results": "game_results",
            "bet_time_result": create_bettime().pk,
        }
        url = reverse('gspin_gameresult_update', args=[gameresult.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BetTimeViewTest(unittest.TestCase):
    '''
    Tests for BetTime
    '''
    def setUp(self):
        self.client = Client()

    def test_list_bettime(self):
        url = reverse('gspin_bettime_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bettime(self):
        url = reverse('gspin_bettime_create')
        data = {
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bettime(self):
        bettime = create_bettime()
        url = reverse('gspin_bettime_detail', args=[bettime.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bettime(self):
        bettime = create_bettime()
        data = {
        }
        url = reverse('gspin_bettime_update', args=[bettime.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomUserViewTest(unittest.TestCase):
    '''
    Tests for CustomUser
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customuser(self):
        url = reverse('gspin_customuser_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customuser(self):
        url = reverse('gspin_customuser_create')
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "custom_user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customuser(self):
        customuser = create_customuser()
        url = reverse('gspin_customuser_detail', args=[customuser.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customuser(self):
        customuser = create_customuser()
        data = {
            "first_name": "first_name",
            "last_name": "last_name",
            "custom_user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('gspin_customuser_update', args=[customuser.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


