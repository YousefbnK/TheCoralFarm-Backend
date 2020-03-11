from django.contrib import admin

# Models

from .models import Coral, Coral_type

admin.site.register(Coral)
admin.site.register(Coral_type)