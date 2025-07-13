from django.urls import path
from ledger.views import create_journal_entry, journal_list

urlpatterns = [
    path('journal/create/', create_journal_entry, name='create_journal_entry'),
    path('journal/list', journal_list, name='journal_list'),
]
