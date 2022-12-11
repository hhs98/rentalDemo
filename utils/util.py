from products.models import Product
from rest_framework import serializers
from datetime import datetime

class Util:
    @staticmethod
    def validate_price(price, from_date, to_date, product_id):
        if price <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        product = Product.objects.get(id=product_id)
        estimated_price = (datetime.strptime(to_date, "%Y-%m-%d") - datetime.strptime(from_date, "%Y-%m-%d")).days * product.price
        if price != estimated_price:
            raise serializers.ValidationError('Price must be equal to estimated price')
        return price
