from django.shortcuts import render, redirect
from ledger.models import Account
from ledger.forms import AccountForm

def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'ledger/account_list.html', {'accounts': accounts})

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'ledger/account_form.html', {'form': form})
