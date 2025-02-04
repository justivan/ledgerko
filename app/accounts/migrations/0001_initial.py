# Generated by Django 5.1.3 on 2025-01-13 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("definitions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("general", "General"),
                            ("cash", "Cash"),
                            ("current account", "Current Account"),
                            ("credit card", "Credit Card"),
                            ("saving account", "Saving Account"),
                            ("investment", "Investment"),
                            ("loan", "Loan"),
                            ("mortgage", "Mortgage"),
                        ],
                        max_length=120,
                        verbose_name="Account Type",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Account Name")),
                (
                    "initial_amount",
                    models.DecimalField(db_default=0, decimal_places=2, max_digits=15),
                ),
                ("exclude_from_report", models.BooleanField(db_default=False)),
                (
                    "currency",
                    models.ForeignKey(
                        max_length=3,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="definitions.currency",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Account",
                "verbose_name_plural": "Accounts",
            },
        ),
        migrations.CreateModel(
            name="TransferRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source_amount", models.DecimalField(decimal_places=4, max_digits=12)),
                ("target_amount", models.DecimalField(decimal_places=4, max_digits=12)),
                ("date", models.DateField()),
                (
                    "source_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transfers_out",
                        to="accounts.account",
                    ),
                ),
                (
                    "source_currency",
                    models.ForeignKey(
                        max_length=3,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="transfers_out",
                        to="definitions.currency",
                    ),
                ),
                (
                    "target_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transfers_in",
                        to="accounts.account",
                    ),
                ),
                (
                    "target_currency",
                    models.ForeignKey(
                        max_length=3,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="transfers_in",
                        to="definitions.currency",
                    ),
                ),
            ],
            options={
                "verbose_name": "Transfer Record",
                "verbose_name_plural": "Transfer Records",
                "db_table": "accounts_transfer_record",
            },
        ),
        migrations.AddConstraint(
            model_name="account",
            constraint=models.UniqueConstraint(
                fields=("user", "name"), name="accounts_account_user_id_name_unique"
            ),
        ),
    ]
