from django import forms
from .models import Lead, Interaction

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'company', 'status']

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['note']
