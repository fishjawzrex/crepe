from .models import *
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
class CrepeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crepe
        fields = "__all__"
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =Item
        fields = "__all__"
class WrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wrap
        fields = "__all__"

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = "__all__"

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = "__all__"

class NutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nut
        fields = "__all__"

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = "__all__"
class SideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Side
        fields = "__all__"