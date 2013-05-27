from django.contrib.gis import admin
from models import Sources, Layers,Maps, Atlases



admin.site.register(Atlases, admin.GeoModelAdmin)
admin.site.register(Sources, admin.GeoModelAdmin)
admin.site.register(Layers, admin.GeoModelAdmin)
admin.site.register(Maps, admin.GeoModelAdmin)
