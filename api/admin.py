from django.contrib import admin

# Models

from .models import Coral, CoralType, Checkout, Order, Profile

admin.site.register(Coral)
admin.site.register(CoralType)
admin.site.register(Checkout)
admin.site.register(Order)
admin.site.register(Profile)