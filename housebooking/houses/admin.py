from django.contrib import admin
from .models import House, HouseImages, Amenity

# Register your models here.
admin.site.register(HouseImages)
admin.site.register(House)
admin.site.register(Amenity)