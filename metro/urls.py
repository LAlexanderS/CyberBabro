from django.urls import path, include
from . import views

app_name = 'metro'

urlpatterns = [
	path('', views.index, name="metro")
]