from django import forms
from ledger.models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
