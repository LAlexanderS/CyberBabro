from django.urls import path, include
from . import views

app_name = 'passengers'

urlpatterns = [
	path('', views.index, name="passengers")
]