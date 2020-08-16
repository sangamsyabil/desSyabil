from django.contrib import admin

from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ['billing_profile', 'name', 'address_line_1', 'city', 'country', 'postal_code', 'address_type']
    list_filter = ['address_type', 'billing_profile', 'country']
    search_fields = ['billing_profile', 'address_line_1', 'city', 'postal_code']


admin.site.register(Address, AddressAdmin)
