from accounts.models import Account, TransferRecord
from definitions.models import Currency
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from .enums import PaymentStatus, PaymentType, TransactionType

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ("category", "name")
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        constraints = [
            models.UniqueConstraint(
                fields=["category", "name"],
                name="ledgers_subcategory_category_id_name_unique",
            )
        ]

    def __str__(self) -> str:
        return f"{self.category}: {self.name}"


class Label(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=120, editable=False)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Transaction(models.Model):
    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
        null=True,
    )
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2, db_default=0)
    currency_code = models.ForeignKey(
        Currency,
        max_length=3,
        on_delete=models.PROTECT,
    )
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    labels = models.ManyToManyField(
        Label,
        db_table="ledgers_transaction_label",
        blank=True,
    )
    date = models.DateTimeField()
    payment_type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
        default=PaymentType.CASH,
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.CLEARED,
    )
    transfer = models.BooleanField(default=False)
    transfer_id = models.ForeignKey(
        TransferRecord,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "ledgers_transaction"
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self) -> str:
        return self.transaction_type
