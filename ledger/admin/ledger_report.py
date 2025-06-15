from django.contrib import admin
from ledger.models import  JournalItem


@admin.register(JournalItem)
class JournalItemAdmin(admin.ModelAdmin):
    list_display = ('journal_entry', 'account', 'debit', 'credit')
    list_filter = ('account',)
    search_fields = ('journal_entry__description', 'account__account_name')
