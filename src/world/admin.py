from django.contrib.gis import admin
from models import WorldBorders

class WorldBordersAmdin(admin.GeoModelAdmin):
    search_fields = ['name']

admin.site.register(WorldBorders, WorldBordersAmdin)
#admin.site.register(WorldBorders, admin.OSMGeoAdmin)