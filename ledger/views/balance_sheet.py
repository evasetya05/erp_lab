from django.shortcuts import render
from django.db.models import Sum, Q
from ledger.models import Account, JournalItem


def calculate_balance(account):
    """Menghitung saldo akun berdasarkan jenis balance type."""
    items = JournalItem.objects.filter(account=account)
    debit_total = items.aggregate(total=Sum('debit'))['total'] or 0
    credit_total = items.aggregate(total=Sum('credit'))['total'] or 0

    print(f"AKUN: {account.account_name} | Debit: {debit_total} | Credit: {credit_total} | Balance Type: {account.balance_type}")

    if account.balance_type == 'Debit':
        return debit_total - credit_total
    else:
        return credit_total - debit_total


def balance_sheet_view(request):
    asset_accounts = Account.objects.filter(account_type='ASSET', active=True)
    liability_accounts = Account.objects.filter(account_type='LIABILITY', active=True)
    equity_accounts = Account.objects.filter(account_type='CAPITAL', active=True)

    assets = []
    liabilities = []
    equities = []

    total_assets = 0
    total_liabilities = 0
    total_equities = 0

    # Hitung aset
    for acc in asset_accounts:
        balance = calculate_balance(acc)
        assets.append({'account': acc, 'balance': balance})
        total_assets += balance

    # Hitung kewajiban
    for acc in liability_accounts:
        balance = calculate_balance(acc)
        liabilities.append({'account': acc, 'balance': balance})
        total_liabilities += balance

    # Hitung ekuitas
    for acc in equity_accounts:
        balance = calculate_balance(acc)
        equities.append({'account': acc, 'balance': balance})
        total_equities += balance

    context = {
        'assets': assets,
        'liabilities': liabilities,
        'equities': equities,
        'total_assets': total_assets,
        'total_liabilities': total_liabilities,
        'total_equities': total_equities,
    }

    return render(request, 'ledger/balance_sheet.html', context)
