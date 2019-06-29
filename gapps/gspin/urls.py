from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'account', api.AccountViewSet)
router.register(r'balance', api.BalanceViewSet)
router.register(r'bet', api.BetViewSet)
router.register(r'accounttopup', api.AccountTopUpViewSet)
router.register(r'betresults', api.BetResultsViewSet)
router.register(r'gameresult', api.GameResultViewSet)
router.register(r'bettime', api.BetTimeViewSet)
router.register(r'customuser', api.CustomUserViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Account
    path('gspin/account/', views.AccountListView.as_view(), name='gspin_account_list'),
    path('gspin/account/create/', views.AccountCreateView.as_view(), name='gspin_account_create'),
    path('gspin/account/detail/<int:pk>/', views.AccountDetailView.as_view(), name='gspin_account_detail'),
    path('gspin/account/update/<int:pk>/', views.AccountUpdateView.as_view(), name='gspin_account_update'),
)

urlpatterns += (
    # urls for Balance
    path('gspin/balance/', views.BalanceListView.as_view(), name='gspin_balance_list'),
    path('gspin/balance/create/', views.BalanceCreateView.as_view(), name='gspin_balance_create'),
    path('gspin/balance/detail/<int:pk>/', views.BalanceDetailView.as_view(), name='gspin_balance_detail'),
    path('gspin/balance/update/<int:pk>/', views.BalanceUpdateView.as_view(), name='gspin_balance_update'),
)

urlpatterns += (
    # urls for Bet
    path('gspin/bet/', views.BetListView.as_view(), name='gspin_bet_list'),
    path('gspin/bet/create/', views.BetCreateView.as_view(), name='gspin_bet_create'),
    path('gspin/bet/detail/<int:pk>/', views.BetDetailView.as_view(), name='gspin_bet_detail'),
    path('gspin/bet/update/<int:pk>/', views.BetUpdateView.as_view(), name='gspin_bet_update'),
)

urlpatterns += (
    # urls for AccountTopUp
    path('gspin/accounttopup/', views.AccountTopUpListView.as_view(), name='gspin_accounttopup_list'),
    path('gspin/accounttopup/create/', views.AccountTopUpCreateView.as_view(), name='gspin_accounttopup_create'),
    path('gspin/accounttopup/detail/<int:pk>/', views.AccountTopUpDetailView.as_view(), name='gspin_accounttopup_detail'),
    path('gspin/accounttopup/update/<int:pk>/', views.AccountTopUpUpdateView.as_view(), name='gspin_accounttopup_update'),
)

urlpatterns += (
    # urls for BetResults
    path('gspin/betresults/', views.BetResultsListView.as_view(), name='gspin_betresults_list'),
    path('gspin/betresults/create/', views.BetResultsCreateView.as_view(), name='gspin_betresults_create'),
    path('gspin/betresults/detail/<slug:slug>/', views.BetResultsDetailView.as_view(), name='gspin_betresults_detail'),
    path('gspin/betresults/update/<slug:slug>/', views.BetResultsUpdateView.as_view(), name='gspin_betresults_update'),
)

urlpatterns += (
    # urls for GameResult
    path('gspin/gameresult/', views.GameResultListView.as_view(), name='gspin_gameresult_list'),
    path('gspin/gameresult/create/', views.GameResultCreateView.as_view(), name='gspin_gameresult_create'),
    path('gspin/gameresult/detail/<int:pk>/', views.GameResultDetailView.as_view(), name='gspin_gameresult_detail'),
    path('gspin/gameresult/update/<int:pk>/', views.GameResultUpdateView.as_view(), name='gspin_gameresult_update'),
)

urlpatterns += (
    # urls for BetTime
    path('gspin/bettime/', views.BetTimeListView.as_view(), name='gspin_bettime_list'),
    path('gspin/bettime/create/', views.BetTimeCreateView.as_view(), name='gspin_bettime_create'),
    path('gspin/bettime/detail/<int:pk>/', views.BetTimeDetailView.as_view(), name='gspin_bettime_detail'),
    path('gspin/bettime/update/<int:pk>/', views.BetTimeUpdateView.as_view(), name='gspin_bettime_update'),
)

urlpatterns += (
    # urls for CustomUser
    path('gspin/customuser/', views.CustomUserListView.as_view(), name='gspin_customuser_list'),
    path('gspin/customuser/create/', views.CustomUserCreateView.as_view(), name='gspin_customuser_create'),
    path('gspin/customuser/detail/<int:pk>/', views.CustomUserDetailView.as_view(), name='gspin_customuser_detail'),
    path('gspin/customuser/update/<int:pk>/', views.CustomUserUpdateView.as_view(), name='gspin_customuser_update'),
)

