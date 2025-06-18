from django.contrib import admin
from .models import Lead, Interaction

class InteractionInline(admin.TabularInline):
    model = Interaction
    extra = 1

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone', 'company')
    list_filter = ('status', 'created_at')
    inlines = [InteractionInline]

admin.site.register(Interaction)
