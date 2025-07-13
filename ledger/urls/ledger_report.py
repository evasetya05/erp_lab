from django.urls import path
from ledger.views.ledger_report import ledger_report
from ledger.views.profit_loss import profit_and_loss_report
urlpatterns = [
    path('report/', ledger_report, name='ledger_report'),  # /report/ --> laporan buku besar
]
