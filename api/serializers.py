from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

# Models
from .models import Coral, CoralType, Checkout, Order


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

# --- Orders Serializers ---#
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["coral", "quantity"]

class CheckoutSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Checkout
        fields = ["order", "user", "date"]


# --- Profile ---#

class ProfileSerializer(serializers.ModelSerializer):
    past_orders = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "past_orders"]

    def get_past_orders(self, obj):
        order = Checkout.objects.filter(user=obj.id, date__lte=date.today())
        return OrderSerializer(order, many=True).data

