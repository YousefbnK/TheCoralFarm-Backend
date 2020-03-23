from django.contrib import admin

# Models

from .models import *
admin.site.register(Coral)
admin.site.register(CoralType)
admin.site.register(OrderCheckout)
admin.site.register(OrderItems)
