from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

# Serializers
from .serializers import *

#  Models
from .models import *

# Permissions
from .permissions import IsOwner


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


# ---  corals type views   ----#
class type_List_View(ListAPIView):
    queryset = Coral_type.objects.all()
    serializer_class = typeListSerializer


# ---  items "corals" views ----#
class Item_List_View(ListAPIView):
    queryset = Coral.objects.all()
    serializer_class = ItemListSerializer

# --- Orders ---#

class Checkout_View(CreateAPIView):
	serializer_class = OrdersSerializer
	permission_classes = [IsAuthenticated]

class Previous_Orders_View(ListAPIView):
	serializer_class = OrdersSerializer 
	permission_classes = [IsAuthenticated, IsOwner]

	def get_queryset(self):
		return Checkout.objects.filter(user=self.request.user, date__lte=datetime.today())


