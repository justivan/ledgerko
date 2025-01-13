from django.contrib import admin

from .models import Category, Label, Subcategory, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    list_filter = ("name",)
    fields = ("name",)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)
    ordering = ("category", "name")
    fields = ("name", "category")


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "slug")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "account",
        "amount",
        "currency_code",
        "subcategory",
        "date",
        "transaction_type",
        "payment_type",
        "payment_status",
        "transfer",
        "transfer_id",
    )
    search_fields = ("account__name", "subcategory__name", "transaction_type")
    list_filter = (
        "transaction_type",
        "payment_type",
        "payment_status",
        "transfer",
        "date",
    )
    ordering = ("-date",)
    date_hierarchy = "date"
    fields = (
        "account",
        "amount",
        "currency_code",
        "subcategory",
        "labels",
        "date",
        "transaction_type",
        "payment_type",
        "payment_status",
        "transfer",
        "transfer_id",
    )
    filter_horizontal = ("labels",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Optional: Custom filtering based on user permissions or logic
        return queryset

    def save_model(self, request, obj, form, change):
        if not obj.id:
            # Optional: Add custom save logic if necessary (e.g., setting default values)
            pass
        super().save_model(request, obj, form, change)
