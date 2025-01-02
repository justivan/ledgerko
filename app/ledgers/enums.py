from django.db import models
from django.utils.translation import gettext_lazy as _


class TransactionType(models.TextChoices):
    INCOME = "income", _("Income")
    EXPENSE = "expense", _("Expense")
    TRANSFER = "transfer", _("Transfer")


class PaymentType(models.TextChoices):
    CASH = "cash", _("Cash")
    DEBIT = "debit", _("Debit Card")
    CREDIT = "credit", _("Credit Card")
    VOUCHER = "voucher", _("Voucher")
    BANK_TRANSFER = "bank transfer", _("Bank Transfer")


class PaymentStatus(models.TextChoices):
    PENDING = "pending", _("Pending")
    CLEARED = "cleared", _("Cleared")
