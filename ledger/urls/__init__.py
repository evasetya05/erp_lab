# ledger/urls/__init__.py

from django.urls import path
from ledger.views.index import index
from ledger.views.ledger_report import ledger_report
from ledger.views.journal_entry import create_or_edit_journal_entry, journal_list

urlpatterns = [
    path('', index, name='ledger_index'),
    path('report/', ledger_report, name='ledger_report'),
    path('journal/create/', create_or_edit_journal_entry, name='create_journal_entry'),
    path('journal/list/', journal_list, name='journal_list'),
    path('journals/<int:journal_id>/edit/', create_or_edit_journal_entry, name='edit_journal'),
]
