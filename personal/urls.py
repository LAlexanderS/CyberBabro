from django.urls import path, include
from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.add_personal_and_shift, name='personal'),
    path('personal-list/', views.personal_list, name='personal_list'),
    path('shift-list/', views.shift_list, name='shift_list'),
]
