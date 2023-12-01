from django.contrib import admin
from .models import Destination,Sub,Booked

# Register your models here.

admin.site.register(Destination)

admin.site.register(Sub)
admin.site.register(Booked)