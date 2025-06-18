# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lead
from .forms import LeadForm, InteractionForm

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.lead = lead
            interaction.save()
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = InteractionForm()
    return render(request, 'leads/lead_detail.html', {'lead': lead, 'form': form})

def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()
            return redirect('lead_detail', pk=lead.pk)
    else:
        form = LeadForm()
    return render(request, 'leads/lead_form.html', {'form': form})
