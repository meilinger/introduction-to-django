from django.contrib.gis import admin
from core.models import TreeSample, TreeSpecies

class TreeSampleAdmin(admin.OSMGeoAdmin):
    list_display = ['treespecies', 'collected_at']
    search_fields = ['treespecies__genus', 'treespecies__species', 'treespecies__common_name']

class TreeSpeciesAdmin(admin.OSMGeoAdmin):
    list_display = ['genus', 'species', 'common_name']
    search_fields = ['genus', 'species', 'common_name']

admin.site.register(TreeSample, TreeSampleAdmin)
admin.site.register(TreeSpecies, TreeSpeciesAdmin)
