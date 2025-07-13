from django.shortcuts import get_object_or_404, render, redirect
from ledger.models import JournalEntry, JournalItem, Account
from django.utils.timezone import now

def create_journal_entry(request):
    if request.method == 'POST':
        date = request.POST.get('date') or now().date()
        description = request.POST.get('description')

        journal = JournalEntry.objects.create(date=date, description=description)

        accounts = request.POST.getlist('account_id[]')
        debits = request.POST.getlist('debit[]')
        credits = request.POST.getlist('credit[]')
        notes = request.POST.getlist('note[]')

        for account_id, debit, credit, note in zip(accounts, debits, credits, notes):
            if not account_id.strip():
                continue

            account = get_object_or_404(Account, pk=account_id)
            JournalItem.objects.create(
                journal_entry=journal,
                account=account,
                debit=debit or 0,
                credit=credit or 0,
                note=note or ''
            )

        return redirect('journal_list')

    return render(request, 'ledger/journal_entry.html', {
        'today': now().date(),
        'accounts': Account.objects.all(),
    })


def journal_list(request):
    journals = JournalEntry.objects.all().order_by('-date', '-id').prefetch_related('items', 'items__account')
    return render(request, 'ledger/journal_list.html', {'journals': journals})
