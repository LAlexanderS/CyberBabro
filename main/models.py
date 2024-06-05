from django.db import models

class Personal(models.Model):
    name = models.CharField(max_length=150, unique=False, blank=False, null=False, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    

    
    class Meta:
        db_table = 'Personal'
        verbose_name = 'сотрудника'
        verbose_name_plural = 'Сотрудники'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = "Сотрудники"
        super(Personal, self).save(*args, **kwargs)
