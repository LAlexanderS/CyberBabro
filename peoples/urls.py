from django.urls import path, include
from . import views

app_name = 'peoples'

urlpatterns = [
	path('', views.index, name="peoples")
]