from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


class Currency(models.Model):
    code = models.CharField(_("Currency Code"), max_length=3, primary_key=True)
    name = models.CharField(_("Currency Name"), max_length=120, unique=True)

    class Meta:
        ordering = ("code",)
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class ExchangeRate(models.Model):
    source_currency = models.ForeignKey(
        Currency,
        max_length=3,
        on_delete=models.CASCADE,
        related_name="source_rates",
        verbose_name=_("Source Currency"),
    )
    target_currency = models.ForeignKey(
        Currency,
        max_length=3,
        on_delete=models.CASCADE,
        related_name="target_rates",
        verbose_name=_("Target Currency"),
    )
    rate = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name=_("Exchange Rate"),
    )
    date = models.DateField()

    class Meta:
        db_table = "definitions_exchange_rate"
        verbose_name_plural = "Exchange Rates"
        constraints = [
            models.UniqueConstraint(
                fields=["source_currency", "target_currency", "date"],
                name="definitions_exchange_rate_source_target_unique",
            )
        ]

    def __str__(self):
        return f"{self.source_currency.code} to {self.target_currency.code}"

    def clean(self):
        if self.source_currency == self.target_currency:
            raise ValidationError("Source and target currencies must be different.")
