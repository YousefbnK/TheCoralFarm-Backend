from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Serializers
from .serializers import *

#  Models
from .models import *

# Permissions
from .permissions import IsOwner


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


# ---  corals type views   ----#
class TypeListView(ListAPIView):
	queryset = CoralType.objects.all()
	serializer_class = typeListSerializer


# ---  items "corals" views ----#
class ItemListView(ListAPIView):
	queryset = Coral.objects.all()
	serializer_class = ItemListSerializer

  
# ---  Orders views   ---#

class OrdersListView(ListAPIView):
	serializer_class = CheckoutListSerializer

	def get_queryset(self):
		return Order_Checkout.objects.filter(user=self.request.user)


class OrdersCreatView(CreateAPIView):
	serializer_class=CreateOrderSerializer


	



	 	


