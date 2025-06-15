from django.shortcuts import render
from ledger.models import Account, JournalItem
from django.contrib.humanize.templatetags.humanize import intcomma



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

        balance = 0  # ✅ Inisialisasi sebelum digunakan
        rows = []
        for item in items:
            balance += item.debit - item.credit
            rows.append({
                'date': item.journal_entry.date,
                'desc': item.journal_entry.description,
                'debit': intcomma(int(item.debit)),
                'credit': intcomma(int(item.credit)),
                'balance': intcomma(int(balance)),
            })


        ledger_data.append({
            'account': account,
            'rows': rows,
        })

    return render(request, 'ledger/ledger_report.html', {
        'ledger_data': ledger_data
    })
