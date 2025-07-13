# ledger/urls.py
from django.urls import path
from ledger.views.journal_edit import journal_edit  # ✅ ini memanggil fungsi dari file journal_edit.py

urlpatterns = [
    path('journal/edit/<int:pk>/', journal_edit, name='journal_edit'),
]
