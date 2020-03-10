from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import *
from .models import *

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


# ---  corals type views   ----#
class type_List_View(ListAPIView):
    queryset = CoralType.objects.all()
    serializer_class = typeListSerializer


# ---  items "corals" views ----#
class Item_List_View(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


