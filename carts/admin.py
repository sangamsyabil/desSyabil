from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'subtotal', 'total', 'updated', 'timestamp']
    list_filter = ['user', 'updated']
    search_fields = ['user', 'updated']


admin.site.register(Cart, CartAdmin)
