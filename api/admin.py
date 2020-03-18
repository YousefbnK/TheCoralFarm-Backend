from django.contrib import admin

# Models

from .models import *
admin.site.register(Coral)
admin.site.register(CoralType)
admin.site.register(Order_Checkout)
admin.site.register(Order_items)
