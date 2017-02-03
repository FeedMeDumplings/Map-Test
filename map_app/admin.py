from django.contrib import admin
from .models import AreaLocation, GasStation, Rest, Store
# Register your models here.

admin.site.register(AreaLocation)
admin.site.register(GasStation)
admin.site.register(Rest)
admin.site.register(Store)
