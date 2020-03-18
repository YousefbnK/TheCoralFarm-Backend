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
		return Checkout.objects.filter(user=self.request.user)


class OrdersCreatView(CreateAPIView):
	serializer_class=CreateOrderSerializer


	



	 	

# class CheckoutView(APIView):
# 	def post(self, request):
# 		serializer = OrdersSerializer(data=request.data, many=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)

# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# queryset = Checkout.objects.all()
	# serializer_class = OrdersSerializer
	# # permission_classes = [IsAuthenticated]

	# def create(self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data, many=True)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.object = serializer.save(force_insert=True)	
	# 	self.post_save(self.objec, created=True)
	# 	headers = self.get_success_headers(serializer.data)
	# 	return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



# --- Profile ---#
# class ProfileView(RetrieveAPIView):
# 	serializer_class = ProfileSerializer 
# 	permission_classes = [IsAuthenticated]


# 	def get_object(self):
# 		return self.request.user.profile




