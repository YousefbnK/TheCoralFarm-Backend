from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

# Models
from .models import Coral, CoralType, OrderCheckout, OrderItem


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
class TypeListSerializer(serializers.ModelSerializer):
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
    image=serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = ["quantity" ,"coral","coralName","coralPrice", "totalPrice","image"]

    def get_coralName(self,obj):
        return obj.coral.name


    def get_coralPrice(self,obj):
        return obj.coral.price

    def get_totalPrice(self,obj):
        total_price=obj.coral.price*obj.quantity
        return total_price

    def get_image(self,obj):
        return obj.coral.image.url




class CheckoutListSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField()
    totalPrice = serializers.SerializerMethodField()
    class Meta:

        model = OrderCheckout
        fields = ["id",'date','user',"totalPrice",'orderItems','pyment_method']


    def get_orderItems(self, obj):
        order = OrderItem.objects.filter(cart=obj.id)
        return CheckoutItemsSerializer(order, many=True).data

    def get_totalPrice(self, obj):
        orders = OrderItem.objects.filter(cart=obj.id)
        totalPrice=0
        for order in orders:
            totalPrice+=(order.coral.price*order.quantity)
        return totalPrice



# --- Orders create Serializers ---#

class CreateOrderSerializer(serializers.ModelSerializer):
    orderItems = CheckoutItemsSerializer(many=True)
    class  Meta:
        model= OrderCheckout
        fields = ['orderItems']

    def create(self, validated_data):
        orderItems = validated_data.pop('orderItems')
        checkout=OrderCheckout.objects.create(**validated_data)
        for item in orderItems:
            OrderItem.objects.create(**item,cart=checkout)
        return checkout
