from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.

#toppings/honey...
class Toppings(APIView):
    def get(self, request):
        toppings = Topping.objects.all()
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Customers(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Orders(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Crepes(APIView):
    def get(self, request):
        crepes = Crepe.objects.all()
        serializer = CrepeSerializer(crepes, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Items(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Wraps(APIView):
    def get(self, request):
        wraps = Wrap.objects.all()
        serializer = WrapSerializer(wraps, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Fruits(APIView):
    def get(self, request):
        fruits = Fruit.objects.all()
        wraps = Wrap.objects.all()
        res = []
        for elem in wraps:
            res.append(elem)
        for elem in fruits:
            res.append(elem)
        
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Nuts(APIView):
    def get(self, request):
        nuts = Nut.objects.all()
        serializer = NutSerializer(nuts, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Beverages(APIView):
    def get(self, request):
        beverages = Beverage.objects.all()
        serializer = BeverageSerializer(beverages, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Sides(APIView):
    def get(self, request):
        sides = Side.objects.all()
        serializer = SideSerializer(sides, many=True)
        return Response(serializer.data)

    def post(self):
        pass