from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "get_type_display",
        "initial_amount",
        "currency",
        "exclude_from_report",
    )

    list_filter = ("type", "currency")
    search_fields = ("name", "user__username")

    def get_type_display(self, obj):
        return obj.get_type_display()

    get_type_display.admin_order_field = "type"
    get_type_display.short_description = "Account Type"


admin.site.register(Account, AccountAdmin)
