from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from .models import Coral, Coral_type, Checkout


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
        model = Coral_type
        fields = ['name', 'image', ]


# ---  corals item Serializers   ----#
class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coral
        fields = "__all__"

# --- Orders Serializers ---#
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
