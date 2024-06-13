from django.urls import path, include
from . import views

app_name = 'Station'

urlpatterns = [
	path('', views.add_all_forms, name="Station")
]