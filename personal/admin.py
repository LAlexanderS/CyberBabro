from django.contrib import admin
from .models import Shift, Personal
from .forms import PersonalForm

class PersonalAdmin(admin.ModelAdmin):
    form = PersonalForm
    list_display = ('ID', 'FIO', 't_n', 'UCHASTOK', 'RANK', 'SEX', 't_tel', 'r_tel', 'zdo_display')
    list_display_links = ('ID', 'FIO')
    list_filter = ('SEX', 'UCHASTOK', 'RANK', 'zdo', 'FIO')
    search_fields = ('last_name', 'first_name', 'FIO', 't_n', 't_tel', 'r_tel')

    def zdo_display(self, obj):
        return 'Да' if obj.zdo else 'Нет'
    zdo_display.short_description = 'Тяжелая работа'

admin.site.register(Personal, PersonalAdmin)

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id_SMENA', 'SMENA', 'date', 'get_inspector_FIO', 'time_work_begin',)
    list_display_links = ('id_SMENA', 'get_inspector_FIO')
    list_filter = ('date', 'SMENA')
    search_fields = ('SMENA', 'id_insp__FIO')
    exclude = ('FIO',)

    def get_inspector_FIO(self, obj):
        return obj.id_insp.FIO if obj.id_insp else 'Не указан'
    get_inspector_FIO.short_description = 'Инспектор'





admin.site.register(Shift, ShiftAdmin)
