from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discounted_price', 'quantity', 'featured',)
    list_filter = ('title', 'price', 'quantity', 'featured',)
    list_editable = ('price', 'discounted_price', 'quantity',)

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
