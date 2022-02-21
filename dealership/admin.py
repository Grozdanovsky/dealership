from unicodedata import name
from django.contrib import admin

from . import models

admin.site.register(models.Type)
admin.site.register(models.Company)
admin.site.register(models.Vehicle)
admin.site.register(models.User)
admin.site.register(models.UserServiceVehicle)