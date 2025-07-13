from django.urls import path, include

urlpatterns = [
    path('', include('ledger.urls.index')),
    path('report/', include('ledger.urls.ledger_report')),
    path('report/', include('ledger.urls.profit_loss')),
    path('journal/', include('ledger.urls.journal_entry')),
    path('journal/', include('ledger.urls.journal_edit')),
    path('accounts/', include('ledger.urls.balance_sheet')),
    path('accounts/', include('ledger.urls.account')),
]
