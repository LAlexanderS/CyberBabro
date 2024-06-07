from django.db import models

class Passengers(models.Model):

    id_pas = models.AutoField(primary_key=True)
    fio_p = models.CharField(max_length=255, verbose_name = 'ФИО Пассажира')
    tep_p = models.CharField(max_length=50, verbose_name = 'Номер телефона')
    sex_p = models.CharField(max_length=8, verbose_name = 'Пол')
    pass_category = models.CharField(max_length=50,verbose_name = 'Категория пасажира')
    dop_inf = models.TextField(blank=True, null=True,verbose_name = 'Дополнительная информация')
    eks = models.BooleanField(verbose_name = 'Наличие кардиостимулятора')

  
    class Meta:
        db_table = 'Passengers'
        verbose_name = 'пассажира'
        verbose_name_plural = 'Пассажиры'
    
    def __str__(self):
        return self.fio_p
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.category = "Пассажиры"	
    #     super(Passengers, self).save(*args, **kwargs)
