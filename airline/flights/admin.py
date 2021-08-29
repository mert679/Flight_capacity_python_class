from django.contrib import admin
from .models import Flights, Airplane
# Register your models here.

admin.site.register(Flights)
admin.site.register(Airplane)