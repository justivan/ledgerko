from django.contrib import admin

from .models import Currency, ExchangeRate


@admin.register(Currency)
class CurrencyModelAdmin(admin.ModelAdmin):
    list_display = ("code", "name")


@admin.register(ExchangeRate)
class ExchangeRateModelAmind(admin.ModelAdmin):
    list_display = ("date", "source_currency", "target_currency", "rate")
