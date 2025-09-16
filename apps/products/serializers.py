from rest_framework import serializers

from apps.products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','product', 'image', 'amount', 'description')
