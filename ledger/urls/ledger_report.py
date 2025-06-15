from django.urls import path
from ledger.views.index import index
from ledger.views.ledger_report import ledger_report

urlpatterns = [
    path('report/', ledger_report, name='ledger_report'),  # /report/ --> laporan buku besar
]
