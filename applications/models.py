from django.db import models
from passengers.models import Passengers
from metro.models import Station


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    id_pas = models.ForeignKey(Passengers, on_delete=models.CASCADE, verbose_name='Пассажир', blank=True, null=True)
    datetime = models.DateTimeField(verbose_name='Дата и время начала заявки')
    tpz = models.DateTimeField(verbose_name='Дата и время окончания заявки')
    time3 = models.DateTimeField(verbose_name='Время встречи с пассажиром',unique=True)
    time4 = models.DateTimeField(verbose_name='Время исполнения заявки')
    tpz = models.DateTimeField(verbose_name='Время регистрации заявки')
    INSP_SEX_M = models.IntegerField(verbose_name='Количество сотрудников мужчин')
    INSP_SEX_F = models.IntegerField(verbose_name='Количество сотрудников женщин')
    TIME_OVER = models.TimeField(verbose_name='Время окончания заявки', blank=True, null=True)
    id_st1 = models.ForeignKey(Station, related_name='departure_station', on_delete=models.CASCADE, verbose_name='Станция отправления')
    id_st2 = models.ForeignKey(Station, related_name='arrival_station', on_delete=models.CASCADE, verbose_name='Станция прибытия')
    status = models.CharField(max_length=50, verbose_name='Текущий статус заявки')
    vokzal = models.BooleanField(verbose_name='Необходимость встретить с воказала', blank=True, null=True)
    dop_inf = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    bag_s = models.BooleanField(verbose_name='Наличие багажа', blank=True, null=True)
    pass_count = models.IntegerField(verbose_name='Количество пассажиров',blank=True, null=True)
    method_p = models.CharField(max_length=50, verbose_name='Метод приёма заявки',blank=True, null=True)

    class Meta:
        db_table = 'Application'
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка {self.id}'

class ApplicationTransfer(models.Model):
    id_adit = models.AutoField(primary_key=True)
    id_bid = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='Заявка')
    time_edit = models.DateTimeField(verbose_name='Время изменения')
    time_s = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name='Изначальное время заявки', to_field='time3', related_name='initial_transfers')
    time_f = models.DateTimeField(verbose_name='Желаемое время')

    class Meta:
        db_table = 'ApplicationTransfer'
        verbose_name = 'Перенос заявки'
        verbose_name_plural = 'Переносы заявок'
   
    def __str__(self):
        return f'Перенос заявки {self.id_adit}'
# Create your models here.
