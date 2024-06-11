from django.urls import path, include
from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.add_personal_and_shift, name='personal'),
   # path('', views.index, name='shift'),
]