from django.apps import AppConfig


class StationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metro'
    verbose_name = 'Станции метрополитена'
