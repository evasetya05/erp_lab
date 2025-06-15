from django.shortcuts import render
from .models import Account, JournalItem
from django.db.models import Sum
from collections import defaultdict
from decimal import Decimal

def ledger_report(request):
    accounts = Account.objects.all().order_by('account_name')
    ledger_data = []

    for account in accounts:
        items = (
            JournalItem.objects
            .filter(account=account)
            .select_related('journal_entry')
            .order_by('journal_entry__date', 'id')
        )

        balance = Decimal('0')
        rows = []
        for item in items:
            balance += item.debit - item.credit
            rows.append({
                'date': item.journal_entry.date,
                'desc': item.journal_entry.description,
                'debit': int(item.debit),
                'credit': int(item.credit),
                'balance': int(balance),
            })


        ledger_data.append({
            'account': account,
            'rows': rows,
        })

    return render(request, 'ledger/ledger_report.html', {'ledger_data': ledger_data})
