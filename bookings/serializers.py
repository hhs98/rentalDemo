from rest_framework import serializers
from .models import Booking
from utils.util import Util

util = Util()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_price(self, value):
        return util.validate_price(value, self.initial_data['from_date'], self.initial_data['to_date'],
                                   self.initial_data['product'])

    def validate(self, data):
        from_date = data['from_date']
        to_date = data['to_date']
        product = data['product']

        if (to_date - from_date).days > product.minimum_rent_period:
            raise serializers.ValidationError("Booking period is greater than minimum booking period")
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
