from rest_framework.generics import CreateAPIView, ListAPIView

# Serializers
from .serializers import *

#  Models
from .models import *


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


