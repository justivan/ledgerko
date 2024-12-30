from django.db import models
from django.utils.translation import gettext_lazy as _


class TransactionType(models.TextChoices):
    INCOME = "INCOME", _("Income")
    EXPENSE = "EXPENSE", _("Expense")


class PaymentType(models.TextChoices):
    CASH = "CASH", _("Cash")
    CARD = "CARD", _("Card")
    BANK_TRANSFER = "BANK_TRANSFER", _("Bank Transfer")


class PaymentStatus(models.TextChoices):
    PENDING = "PENDING", _("Pending")
    COMPLETED = "COMPLETED", _("Completed")
    FAILED = "FAILED", _("Failed")
