from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyModelAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
