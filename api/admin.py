from django.contrib import admin

# Models

from .models import Item, CoralType

admin.site.register(Item)
admin.site.register(CoralType)