from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    path('login/', UserLoginView.as_view() , name='login'),

     #  ----  registration urls ----  # 
    path('register/', UserCreateAPIView.as_view(), name='register'),

     #  ----  API urls ----  # 
    path('coraltype/', type_List_View.as_view(), name='type_list'),
    path('coraltype/corals', Item_List_View.as_view(), name='item_list'),
]


