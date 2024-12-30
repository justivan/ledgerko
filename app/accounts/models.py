from definitions.models import Currency
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Account(models.Model):
    class AccountTypes(models.TextChoices):
        GENERAL = "General"
        CASH = "Cash"
        CURRENT_ACCOUNT = "Current Account"
        CREDIT_CARD = "Credit Card"
        SAVING_ACCOUNT = "Saving Account"
        INVESTMENT = "Investment"
        LOAN = "Loan"
        MORTGAGE = "Mortgage"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.CharField(max_length=120, choices=AccountTypes)
    name = models.CharField(max_length=120)
    initial_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        db_default=0,
    )
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    exclude_from_report = models.BooleanField(db_default=False)

    class Meta:
        unique_together = ("user", "name")

    def __str__(self) -> str:
        return self.get_type_display()


class TransferRecord(models.Model):
    source_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="transfers_out",
    )
    target_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="transfers_in",
    )
    amount = models.DecimalField(max_digits=12, decimal_places=4)
    date = models.DateField()

    class Meta:
        db_table = "accounts_transfer_record"
        verbose_name = "Transfer Record"
        verbose_name_plural = "Transfer Records"

    def __str__(self):
        return f"{self.source_account} to {self.target_account}"
