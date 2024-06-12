from django.contrib import admin
from .models import Application, ApplicationTransfer


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'id_pas', 'datetime', 'time3', 'time4', 'tpz',
        'INSP_SEX_M', 'INSP_SEX_F', 'TIME_OVER', 'id_st1', 'id_st2',
        'status', 'vokzal', 'dop_inf', 'bag_s', 'pass_count', 'method_p'
    )
    list_display_links = ('id', 'id_pas')
    list_filter = ('datetime', 'status', 'id_st1', 'id_st2')
    search_fields = ('id_pas__fio_p', 'status')

class ApplicationTransferAdmin(admin.ModelAdmin):
    list_display = ('id_adit', 'id_bid', 'time_edit', 'get_time3', 'time_f')
    list_display_links = ('id_adit', 'id_bid')
    list_filter = ('time_edit',)
    search_fields = ('id_bid__id',)

    def get_time3(self, obj):
        return obj.time_s.time3
    get_time3.short_description = 'Изначальное время заявки'

admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationTransfer, ApplicationTransferAdmin)






# Register your models here.
