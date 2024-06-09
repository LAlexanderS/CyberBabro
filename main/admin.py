from django.contrib import admin
from .models import Personalapplication

class PersonalapplicationAdmin(admin.ModelAdmin):
    list_display = ('id_pa', 'person', 'application')
    list_display_links = ('id_pa', 'person', 'application')
    list_filter = ('id_pa', 'person', 'application')
    search_fields = ('id_pa', 'person', 'application')

admin.site.register(Personalapplication, PersonalapplicationAdmin)
