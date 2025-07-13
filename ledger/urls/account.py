from django.urls import path
from ledger.views import account_list, account_create

urlpatterns = [
    path('accounts/', account_list, name='account_list'),  # ✅ BENAR
    path('accounts/new/', account_create, name='account_create'),  # ✅ BENAR
]
