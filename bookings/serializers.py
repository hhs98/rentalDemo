from rest_framework import serializers
from .models import Booking
from products.models import Product
from datetime import datetime


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        from_date = datetime.strptime(self.initial_data['from_date'], '%Y-%m-%d')
        to_date = datetime.strptime(self.initial_data['to_date'], '%Y-%m-%d')
        product = Product.objects.get(id=self.initial_data['product'])
        estimated_price = (to_date - from_date).days * product.price
        if value != estimated_price:
            raise serializers.ValidationError('Price must be equal to estimated price')
        return value

    def validate(self, data):
        from_date = data['from_date']
        to_date = data['to_date']
        product = data['product']
        if from_date >= to_date:
            raise serializers.ValidationError('From date must be before to date')
        if not product.availability:
            raise serializers.ValidationError('Product is not available')
        return data

    def create(self, validated_data):
        product = validated_data['product']
        product.availability = False
        product.save()
        return Booking.objects.create(**validated_data)
