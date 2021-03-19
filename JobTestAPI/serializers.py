from rest_framework import serializers
from .models import *


class CarsSer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    ModelName = serializers.CharField(max_length=50)
    BrandName = serializers.CharField(max_length=50, required=False)
    def create(self, validated_data):
        return Cars.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ModelName = validated_data.get('ModelName', instance.ModelName)
        instance.BrandName = validated_data.get('BrandName', instance.BrandName)
        instance.save()
        return instance

class DealerSer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    CompanyName = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return Dealer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.CompanyName = validated_data.get('CompanyName', instance.CompanyName)
        instance.save()
        return instance

class ComparinSer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    DealerId = serializers.IntegerField()
    CarId = serializers.IntegerField()
    Price = serializers.FloatField()
    Quantity = serializers.IntegerField()
    IsNew = serializers.BooleanField(required=False)
    def create(self, validated_data):
        return Comparing.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.DealerId = validated_data.get('DealerId', instance.DealerId)
        instance.CarId = validated_data.get('CarId', instance.CarId)
        instance.Price = validated_data.get('Price', instance.Price)
        instance.Quantity = validated_data.get('Quantity', instance.Quantity)
        instance.IsNew = validated_data.get('IsNew', instance.IsNew)
        instance.save()
        return instance
