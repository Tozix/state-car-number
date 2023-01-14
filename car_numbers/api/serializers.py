from rest_framework import serializers

from .models import CarNumer


class CarNumerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'plate',)
        model = CarNumer
