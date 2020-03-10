from django.urls import path
from .views import UserCreateAPIView, UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', UserLoginView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]