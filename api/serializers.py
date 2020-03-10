from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from .models import Item, CoralType


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


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user_obj = User.objects.get(username=username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)
        data["access"] = token

        return data

# ---  corals type Serializers   ----#
class typeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoralType
        fields = ['name', 'image', ]


# ---  corals item Serializers   ----#
class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

