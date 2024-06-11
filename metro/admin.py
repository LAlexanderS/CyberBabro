from django.contrib import admin
from .models import Line,Station,Stationtime,Transfertime

class LineAdmin(admin.ModelAdmin):
    list_display = ('id_line', 'name_line')
    list_display_links = ('id_line', 'name_line')
    search_fields = ['name_line']

admin.site.register(Line, LineAdmin)



class StationAdmin(admin.ModelAdmin):
    list_display = ('id_station', 'name_station','line')
    list_display_links = ('id_station', 'name_station','line')
    list_filter = ('name_station','line')
    search_fields = ('name_station', 'line')

admin.site.register(Station, StationAdmin)

class StationtimeAdmin(admin.ModelAdmin):
    list_display = ('id_st_time', 'st_time')
    list_display_links = ['id_st_time']
    search_fields = ['id_st_time']


admin.site.register(Stationtime,StationtimeAdmin)

class TransfertimeAdmin(admin.ModelAdmin):
    list_display = ('id_t_time', 'transfer_time')
    list_display_links = ['id_t_time']
    search_fields = ['id_t_time']


admin.site.register(Transfertime,TransfertimeAdmin)




# Register your models here.
