from django.db import models
from personal.models import Personal
from applications.models import Application

class Personalapplication(models.Model):
    id_pa = models.AutoField(primary_key=True)
    person = models.ForeignKey(Personal, related_name='person', on_delete=models.CASCADE, verbose_name='Сотрудник', to_field='ID')
    application = models.ForeignKey(Application, related_name='application', on_delete=models.CASCADE, verbose_name='Заявка', to_field='id')

    class Meta:
        db_table = 'Personalapplication'
        verbose_name = 'Заявки сотрудника'
        verbose_name_plural = 'Заявки сотрудника'
