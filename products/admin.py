from django.contrib import admin

from .models import Product, Category


# from .models import Product, ProductFile

#
# class ProductFileInline(admin.TabularInline):
#     model = ProductFile
#     extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discounted_price', 'quantity', 'featured', 'is_digital')
    list_filter = ('title', 'price', 'quantity', 'featured', 'is_digital')
    list_editable = ('price', 'discounted_price', 'quantity',)

    prepopulated_fields = {'slug': ('title',)}


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'slug', 'is_digital']
#     inlines = [ProductFileInline]
#
#     class Meta:
#         model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
