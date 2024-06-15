from django.contrib import admin
from .models import Shift,Personal

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id_SMENA', 'SMENA', 'date','get_inspector_FIO', 'time_work_begin_display', 'time_work_end_display')
    list_display_links = ('id_SMENA','get_inspector_FIO')
    list_filter = ('date', 'SMENA')
    search_fields = ('SMENA', 'id_insp__FIO')
    exclude = ('FIO',)

    def save_model(self, request, obj, form, change):
        # Create initials from first_name and second_name
        first_initial = obj.first_name[0] + '.' if obj.first_name else ''
        second_initial = obj.second_name[0] + '.' if obj.second_name else ''
        
        # Combine last name with initials
        obj.FIO = f'{obj.last_name} {first_initial}{second_initial}'.strip()
        super().save_model(request, obj, form, change)

    def get_inspector_FIO(self, obj):
        return obj.id_insp.FIO if obj.id_insp else 'Не указан'
    get_inspector_FIO.short_description = 'Инспектор'

    def time_work_begin_display(self, obj):
        return obj.time_work_begin.strftime('%H:%M')
    time_work_begin_display.short_description = 'Начало рабочего дня'

    def time_work_end_display(self, obj):
        return obj.time_work_end.strftime('%H:%M')
    time_work_end_display.short_description = 'Окончание рабочего дня'
    
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('ID','FIO', 't_n', 'UCHASTOK', 'RANK', 'SEX', 't_tel', 'r_tel', 'zdo_display')
    list_display_links = ('ID','FIO')
    list_filter = ('SEX', 'UCHASTOK', 'RANK', 'zdo','FIO')
    search_fields = ('last_name', 'first_name','FIO', 't_n', 't_tel', 'r_tel')

    def zdo_display(self, obj):
        return 'Да' if obj.zdo else 'Нет'
    zdo_display.short_description = 'Тяжелая работа'			

admin.site.register(Personal,PersonalAdmin)
admin.site.register(Shift, ShiftAdmin)
