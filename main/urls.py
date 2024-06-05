from django.urls import path, include
from main import views

app_name = 'events_available'

urlpatterns = [
	path('', views.index, name="index")
]