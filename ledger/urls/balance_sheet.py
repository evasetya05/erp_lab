from django.urls import path
from ledger.views.balance_sheet import balance_sheet_view

urlpatterns = [
    path('ledger/report/balance-sheet/', balance_sheet_view, name='balance_sheet'),
]
