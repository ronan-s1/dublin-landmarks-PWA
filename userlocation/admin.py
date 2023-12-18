# from django.contrib import admin
from django.contrib.gis import admin
from .models import Profile, Landmark

admin.site.register(Profile)
admin.site.register(Landmark, admin.ModelAdmin)
# admin.site.register(Landmark, admin.OSMGeoAdmin)


