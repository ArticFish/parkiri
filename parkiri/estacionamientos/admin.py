from django.contrib import admin

# Register your models here.
from .models import tipoc,estadoe,estacionamiento,estadoc,reserva
# Register your models here.
admin.site.register(tipoc)
admin.site.register(estadoe)
admin.site.register(estacionamiento)
admin.site.register(estadoc)
admin.site.register(reserva)

