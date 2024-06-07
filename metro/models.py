from django.db import models

class Station(models.Model):
    id_station = models.AutoField(primary_key=True)
    name_station = models.CharField(max_length=255,verbose_name='Название станции')
    name_line = models.CharField(max_length=255,verbose_name='Название линии метро')

    class Meta:
        db_table = 'Station'
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
       	

    def __str__(self):
        return self.name_station
    

