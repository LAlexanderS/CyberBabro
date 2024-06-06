from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),  
    path('peoples/', include('peoples.urls', namespace='peoples')),
    path('personal/', include('personal.urls', namespace='personal'))
    
]

if settings.DEBUG: 
	urlpatterns += [
		path("__debug__/", include("debug_toolbar.urls")),
    ]
