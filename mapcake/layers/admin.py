from django.contrib.gis import admin
from layers.models import Layers

admin.site.register(Layers, admin.GeoModelAdmin)