from django.urls import path
from ledger.views.profit_loss import profit_and_loss_report

urlpatterns = [
    path('report/profit-loss/', profit_and_loss_report, name='profit_loss_report'),  # laporan laba rugi
]
