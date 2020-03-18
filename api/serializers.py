from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

# Models
from .models import Coral, CoralType, Order_Checkout, Order_items


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        print(validated_data)
        return validated_data



# ---  corals type Serializers   ----#
class typeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoralType
        fields = ['name', 'image', ]


# ---  corals item Serializers   ----#
class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coral
        fields = "__all__"

        

# --- Orders list Serializers ---#

class CheckoutItemsSerializer(serializers.ModelSerializer):
    coralName=serializers.SerializerMethodField()
    coralPrice=serializers.SerializerMethodField()
    totalPrice=serializers.SerializerMethodField()

    class Meta:
        model = Order_items
        fields = ["quantity" ,"coral","coralName","coralPrice", "totalPrice"]
    
    def get_coralName(self,obj):
        return obj.coral.name


    def get_coralPrice(self,obj):
        return obj.coral.price

    def get_totalPrice(self,obj):
        total_price=obj.coral.price*obj.quantity
        return total_price



class CheckoutListSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    class Meta:

        model = Order_Checkout
        fields = ['date','user','order_items']

    def get_order_items(self, obj):
        order = Order_items.objects.filter(cart=obj.id)
        return CheckoutItemsSerializer(order, many=True).data



# --- Orders create Serializers ---#

class CreateOrderSerializer(serializers.ModelSerializer):
    order_items = CheckoutItemsSerializer(many=True)
    class  Meta:
        model= Order_Checkout
        fields = ['user','order_items']

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        checkout=Order_Checkout.objects.create(**validated_data)
        for item in order_items:
            Order_items.objects.create(**item,cart=checkout)
        return checkout









