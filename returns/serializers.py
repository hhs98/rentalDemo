from rest_framework import serializers
from utils.util import Util
from .models import Return

util = Util()


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = '__all__'

    def validate_price(self, value):
        return util.validate_price(value, self.initial_data['from_date'], self.initial_data['to_date'],
                                   self.initial_data['product'])

    def validate(self, data):
        from_date = data['from_date']
        to_date = data['to_date']
        product = data['product']
        if from_date >= to_date:
            raise serializers.ValidationError('From date must be before to date')
        if product.availability:
            raise serializers.ValidationError('Product is not rented')
        return data

    def create(self, validated_data):
        product = validated_data['product']
        product.availability = True
        product.needing_repair = validated_data['needs_repair']

        if product.type == 'meter':
            product.durability -= (validated_data['to_date'] - validated_data['from_date']).days * 2
            product.durability -= validated_data['mileage_used'] // 10 * 2
            product.mileage += validated_data['mileage_used']
        elif product.type == 'plain':
            product.durability -= (validated_data['to_date'] - validated_data['from_date']).days

        product.save()
        return Return.objects.create(**validated_data)
