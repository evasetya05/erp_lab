from django.shortcuts import render
from ledger.models import Account, JournalItem
from django.db.models import Sum

def profit_and_loss_report(request):
    # Ambil akun aktif bertipe INCOME dan EXPENSES
    income_accounts = Account.objects.filter(account_type='INCOME', active=True)
    expense_accounts = Account.objects.filter(account_type='EXPENSES', active=True)

    # Hitung total pendapatan
    total_income = sum(
        JournalItem.objects.filter(account=acc).aggregate(Sum('credit'))['credit__sum'] or 0
        for acc in income_accounts
    )

    # Hitung total pengeluaran
    total_expense = sum(
        JournalItem.objects.filter(account=acc).aggregate(Sum('debit'))['debit__sum'] or 0
        for acc in expense_accounts
    )

    net_income = total_income - total_expense

    return render(request, 'ledger/profit_loss.html', {
        'total_income': total_income,
        'total_expense': total_expense,
        'net_income': net_income,
    })
