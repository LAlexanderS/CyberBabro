from django.db import models

class Passengers(models.Model):
    name = models.CharField(max_length=150, unique=False, blank=False, null=False, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
  
    class Meta:
        db_table = 'Passengers'
        verbose_name = 'пассажира'
        verbose_name_plural = 'Пассажиры'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = "Пассажиры"	
        super(Passengers, self).save(*args, **kwargs)
