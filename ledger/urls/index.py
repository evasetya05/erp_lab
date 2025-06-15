from django.urls import path
from ledger.views.index import index
from ledger.views.ledger_report import ledger_report

urlpatterns = [
    path('', index, name='index'),  # / --> halaman utama
]
