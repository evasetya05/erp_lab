from django.shortcuts import render, get_object_or_404, redirect
from ledger.models import JournalEntry, JournalItem, Account

def journal_edit(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk)

    # GANTI ini:
    # journal_items = journal.items.all()
    # DENGAN:
    journal_items = JournalItem.objects.filter(journal_entry=journal)

    if request.method == 'POST':
        description = request.POST.get('description')
        is_posted = request.POST.get('post') == '1'

        journal.description = description
        journal.is_posted = is_posted
        journal.save()

        # Hapus semua item
        journal.items.all().delete()

        # Ambil ulang data form
        account_ids = request.POST.getlist('account_id[]')
        debits = request.POST.getlist('debit[]')
        credits = request.POST.getlist('credit[]')
        notes = request.POST.getlist('note[]')


        for account_id, debit, credit, note in zip(account_ids, debits, credits, notes):
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

    return render(request, 'ledger/journal_edit.html', {
        'journal': journal,
        'journal_items': journal_items,
        'accounts': Account.objects.all()
    })


print("Journal:", JournalItem)
print("Jumlah item:", JournalItem.objects.count())
for i in JournalItem.objects.all():
    print(f"Akun: {i.account}, Debit: {i.debit}, Kredit: {i.credit}, Note: {i.note}")
