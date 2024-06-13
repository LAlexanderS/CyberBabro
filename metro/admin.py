from django.contrib import admin
from .models import Station,Stationtime,Transfertime

# class LineAdmin(admin.ModelAdmin):
    # list_display = ('id_line', 'name_line')
    # list_display_links = ('id_line', 'name_line')
    # search_fields = ['name_line']

# admin.site.register(LineAdmin)



class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_station','name_line')
    list_display_links = ('id', 'name_station','name_line')
    list_filter = ('name_station','name_line')
    search_fields = ('name_station', 'name_line')


admin.site.register(Station, StationAdmin)

class StationtimeAdmin(admin.ModelAdmin):
     list_display = ('id_st_time', 'time')
     list_display_links = ['id_st_time']
     search_fields = ['id_st_time']


admin.site.register(Stationtime,StationtimeAdmin)

class TransfertimeAdmin(admin.ModelAdmin):
    list_display = ('id_t_time', 'time')
    list_display_links = ['id_t_time']
    search_fields = ['id_t_time']


admin.site.register(Transfertime,TransfertimeAdmin)




# Register your models here.
