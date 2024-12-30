from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)
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
        verbose_name_plural = "Subcategories"
        ordering = ("category", "name")
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

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Transaction(models.Model):
    pass
