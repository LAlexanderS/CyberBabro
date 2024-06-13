from django.contrib import admin
from .models import Shift,Personal

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id_SMENA', 'id_insp_display', 'SMENA', 'date', 'time_work_begin_display', 'time_work_end_display')
    list_display_links = ('id_SMENA','id_insp_display')
    list_filter = ('date', 'SMENA')
    search_fields = ('SMENA', 'id_insp__ID')

    def id_insp_display(self, obj):
        return obj.id_insp
    id_insp_display.short_description = 'Инспектор'

    def time_work_begin_display(self, obj):
        return obj.time_work_begin.strftime('%H:%M')
    time_work_begin_display.short_description = 'Начало рабочего дня'

    def time_work_end_display(self, obj):
        return obj.time_work_end.strftime('%H:%M')
    time_work_end_display.short_description = 'Окончание рабочего дня'
    
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('ID', 't_n', 'UCHASTOK', 'RANK', 'SEX', 't_tel', 'r_tel', 'zdo_display')
    list_display_links = ['ID']
    list_filter = ('SEX', 'UCHASTOK', 'RANK', 'zdo')
    search_fields = ('last_name', 'first_name', 't_n', 't_tel', 'r_tel')

    def zdo_display(self, obj):
        return 'Да' if obj.zdo else 'Нет'
    zdo_display.short_description = 'Тяжелая работа'			

admin.site.register(Personal,PersonalAdmin)
admin.site.register(Shift, ShiftAdmin)
