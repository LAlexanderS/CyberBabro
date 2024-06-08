from django.db import models
from passengers.models import Passengers
from metro.models import Station


class Appication(models.Model):
    id_z = models.AutoField(primary_key=True)
    id_pas = models.ForeignKey(Passengers, on_delete=models.CASCADE, verbose_name='Пассажир')
    datetime = models.DateTimeField(verbose_name='Дата и время начала заявки')
    in_p = models.DateTimeField(verbose_name='Время встречи с пассажиром')
    out_p = models.DateTimeField(verbose_name='Время исполнения заявки')
    tpz = models.DateTimeField(verbose_name='Время регистрации заявки')
    insp_sex_m = models.IntegerField(verbose_name='Количество сотрудников мужчин')
    insp_sex_f = models.IntegerField(verbose_name='Количество сотрудников женщин')
    time_over = models.TimeField(verbose_name='Время окончания заявки', blank=True, null=True)
    id_st1 = models.ForeignKey(Station, related_name='departure_station', on_delete=models.CASCADE, verbose_name='Станция отправления')
    id_st2 = models.ForeignKey(Station, related_name='arrival_station', on_delete=models.CASCADE, verbose_name='Станция прибытия')
    status = models.CharField(max_length=50, verbose_name='Текущий статус заявки')
    vokzal = models.BooleanField(default=False, verbose_name='Необходимо встретить с вокзала')
    dop_inf = models.TextField(verbose_name='Дополнительная информация', blank=True, null=True)
    bag_s = models.BooleanField(verbose_name='Наличие багажа', blank=True, null=True)
    pass_count = models.IntegerField(verbose_name='Количество пассажиров')
    method_p = models.CharField(max_length=50, verbose_name='Метод приёма заявки')

    class Meta:
        db_table = 'Appication'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Appication {self.id_z}'

class AppicationTransfer(models.Model):
    id_adit = models.AutoField(primary_key=True)
    id_bid = models.ForeignKey(Appication, on_delete=models.CASCADE, verbose_name='Заявка')
    time_edit = models.DateTimeField(verbose_name='Время изменения')
    time_s = models.DateTimeField(verbose_name='Изначальное время')
    time_f = models.DateTimeField(verbose_name='Желаемое время')

    class Meta:
        db_table = 'AppicationTransfer'
        verbose_name = 'Перенос заявки'
        verbose_name_plural = 'Переносы заявок'

    def __str__(self):
        return f'Transfer {self.id_adit}'
# Create your models here.
