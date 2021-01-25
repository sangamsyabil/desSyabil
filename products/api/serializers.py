from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = "slug"

    def get_label(self, obj):
        return obj.get_label_display()

    def get_subcategory(self, obj):
        return obj.get_subcategory_display()

    def get_brand(self, obj):
        return obj.get_brand_display()
