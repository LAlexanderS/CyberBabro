from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),  
    path('passengers/', include('passengers.urls', namespace='passengers')),
    path('personal/', include('personal.urls', namespace='personal')),
    path('applications/', include('applications.urls', namespace='applications')),
    path('user/', include('users.urls', namespace='user')),
]

if settings.DEBUG: 
	urlpatterns += [
		path("__debug__/", include("debug_toolbar.urls")),
    ]
