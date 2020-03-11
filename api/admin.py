from django.contrib import admin

# Models

from .models import Coral, CoralType

admin.site.register(Coral)
admin.site.register(CoralType)