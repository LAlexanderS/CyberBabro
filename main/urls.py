from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('distribute-tasks/', views.distribute_tasks, name='distribute_tasks'),
    path('run-scheduler/', views.run_scheduler, name='run_scheduler'),  # Новый маршрут для запуска планировщика
]

