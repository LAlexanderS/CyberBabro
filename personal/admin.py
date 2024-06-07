from django.contrib import admin

from .models import Personal
from .models import Shift


admin.site.register(Personal)
admin.site.register(Shift)

