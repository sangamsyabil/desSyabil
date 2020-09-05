from django.contrib import admin

from .models import Product, Category, SubCategory, Brand


# from .models import Product, ProductFile

#
# class ProductFileInline(admin.TabularInline):
#     model = ProductFile
#     extra = 1

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_display_links = ('name', 'category',)
    list_filter = ('name', 'category',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discounted_price', 'quantity', 'featured', 'subcategory')
    list_filter = ('title', 'price', 'quantity', 'featured', 'subcategory')
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
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Brand, BrandAdmin)
