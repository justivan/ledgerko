from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    code = models.CharField(_("Currency Code"), max_length=3, primary_key=True)
    name = models.CharField(_("Currency Name"), max_length=120, unique=True)

    class Meta:
        ordering = ("code",)
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"
