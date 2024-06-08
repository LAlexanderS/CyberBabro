from django.contrib import admin
from .models import Station

class StationAdmin(admin.ModelAdmin):
    list_display = ('id_station', 'name_station', 'name_line')
    list_display_links = ('id_station', 'name_station')
    list_filter = ('name_line',)
    search_fields = ('name_station', 'name_line')

admin.site.register(Station, StationAdmin)


# Register your models here.
