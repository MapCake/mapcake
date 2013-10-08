from django.contrib.gis import admin
from models import Sources, Layers
from map.models import Maps
from atlas.models import Atlases
from layers.models import Sources



admin.site.register(Atlases, admin.GeoModelAdmin)
admin.site.register(Sources, admin.GeoModelAdmin)
admin.site.register(Layers, admin.GeoModelAdmin)
admin.site.register(Maps, admin.GeoModelAdmin)
