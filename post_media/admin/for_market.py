from django.contrib import admin
from post_media.models.for_market import Market


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    name = ('name')
    description = ('description')