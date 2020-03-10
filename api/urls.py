from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    path('login/', UserLoginView.as_view() , name='login'),

     #  ----  registration urls ----  # 
    path('register/', UserCreateAPIView.as_view(), name='register'),
]


#   ----- comments ------ # 
#   why do we have the url inside our app ??? 