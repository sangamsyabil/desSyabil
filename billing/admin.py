from django.contrib import admin

from .models import BillingProfile, Card, Charge


class BillingProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer_id', 'update', 'timestamp']
    list_filter = ['user']
    search_fields = ['user']


admin.site.register(BillingProfile, BillingProfileAdmin)
admin.site.register(Card)
admin.site.register(Charge)
