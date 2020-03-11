
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Serializers

from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import *
from .models import *


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request):
		user_data = request.data 
		serializer = UserLoginSerializer(data=user_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)

		return Response(serializer.errors, HTTP_400_BAD_REQUEST)

# ---  corals type views   ----#
class type_List_View(ListAPIView):
    queryset = Coral_type.objects.all()
    serializer_class = typeListSerializer


# ---  items "corals" views ----#
class Item_List_View(ListAPIView):
    queryset = Coral.objects.all()
    serializer_class = ItemListSerializer


