from django.contrib import admin
from .models import Shift,Personal

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id_smena', 'id_insp_display', 'smena', 'date', 'time_work_begin_display', 'time_work_end_display')
    list_display_links = ('id_smena',)
    list_filter = ('date', 'smena')
    search_fields = ('smena', 'id_insp__id_personal')

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
    list_display = ('id_personal', 'full_name_initials', 't_n', 'uch', 'rank', 'sex', 't_tel', 'r_tel', 'zdo_display')
    list_display_links = ('id_personal', 'full_name_initials')
    list_filter = ('sex', 'uch', 'rank', 'zdo')
    search_fields = ('last_name', 'first_name', 't_n', 't_tel', 'r_tel')

    def zdo_display(self, obj):
        return 'Да' if obj.zdo else 'Нет'
    zdo_display.short_description = 'Тяжелая работа'			

admin.site.register(Personal,PersonalAdmin)
admin.site.register(Shift, ShiftAdmin)
