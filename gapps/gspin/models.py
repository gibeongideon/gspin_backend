from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import FloatField
from django.db.models import IntegerField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Account(models.Model):

    # Fields
    account_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    # Relationship Fields
    custom_user = models.ForeignKey(
        'gspin.CustomUser',
        on_delete=models.CASCADE, related_name="accounts", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_account_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_account_update', args=(self.pk,))


class Balance(models.Model):

    # Fields
    balance = models.FloatField(max_length=255 ,default =0)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    account = models.ForeignKey(
        'gspin.Account',
        on_delete=models.CASCADE, related_name="balances"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_balance_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_balance_update', args=(self.pk,))


class Bet(models.Model):

    # Fields
    bet_amount = models.FloatField(max_length=255 )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default =True)
    bet_choice = models.CharField(max_length=30)

    # Relationship Fields
    account = models.ForeignKey(
        'gspin.Account',
        on_delete=models.CASCADE, related_name="bets"
    )
    bet_time = models.OneToOneField(
        'gspin.BetTime',
        on_delete=models.CASCADE, related_name="bets"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_bet_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_bet_update', args=(self.pk,))


class AccountTopUp(models.Model):

    # Fields
    topup_amount = models.FloatField(max_length=255)
    topup_time = models.DateTimeField(auto_now_add=True, editable=False)

    # Relationship Fields
    account_to_topup = models.ForeignKey(
        'gspin.Account',
        on_delete=models.CASCADE, related_name="accounttopups"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_accounttopup_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_accounttopup_update', args=(self.pk,))


class BetResults(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    bet_result = models.ForeignKey(
        'gspin.Bet',
        on_delete=models.CASCADE, related_name="betresultss", blank=True, null=True
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('gspin_betresults_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('gspin_betresults_update', args=(self.slug,))


class GameResult(models.Model):

    # Fields
    game_results = models.CharField(max_length=255)
    start_time = models.DateTimeField(auto_now_add=True, editable=False)
    end_time = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    bet_time_result = models.OneToOneField(
        'gspin.BetTime',
        on_delete=models.CASCADE, related_name="gameresults"
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_gameresult_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_gameresult_update', args=(self.pk,))


class BetTime(models.Model):

    # Fields
    start_time = models.DateTimeField(auto_now_add=True, editable=False)
    end_time = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_bettime_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_bettime_update', args=(self.pk,))


class CustomUser(models.Model):

    # Fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    custom_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="customusers", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('gspin_customuser_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('gspin_customuser_update', args=(self.pk,))


