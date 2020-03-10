from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
     #  ----  registration urls ----  # 
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]


#   ----- comments ------ # 
#   why do we have the url inside our app ??? 