from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    path('login/', TokenObtainPairView.as_view() , name='login'),

     #  ----  registration urls ----  # 
    path('register/', UserCreateAPIView.as_view(), name='register'),

     #  ----  API urls ----  # 
    path('coraltype/', TypeListView.as_view(), name='type_list'),
    path('coraltype/corals/', ItemListView.as_view(), name='item_list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('order/create', CheckoutView.as_view(), name='new-order')
]


