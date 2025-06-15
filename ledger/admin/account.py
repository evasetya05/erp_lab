from django.contrib import admin
from ledger.models import Account, JournalEntry, JournalItem

class JournalItemInline(admin.TabularInline):
    model = JournalItem
    extra = 1

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_type', 'account_name', 'coa', 'balance_type', 'active', 'locked']
    list_display_links = ['account_name']  # agar bisa diklik ke detail
    search_fields = ['account_name', 'account_type', 'coa']
    list_filter = ['account_type', 'balance_type', 'active', 'locked']
    ordering = ['account_type', 'account_name']

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'short_description', 'created_at']
    list_display_links = ['date', 'short_description']
    inlines = [JournalItemInline]

    def short_description(self, obj):
        return obj.description[:50]
    short_description.short_description = 'Description'
