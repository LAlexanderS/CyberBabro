from django.db import models

class Passengers(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    CAT_CHOICES = [
        ('ИЗТ', 'Инвалид по зрению'),
        ('ИЗ', 'Инвалид по зрению с остаточным зрением'),
        ('ИС', 'Инвалид по слуху'),
        ('ИК', 'Инвалид колясочник'),
        ('ИО', 'Инвалид опорник'),
        ('ДИ', 'Ребенок инвалид'),
        ('ПЛ', 'Пожилой человек'),
        ('РД', 'Родители с детьми'),
        ('РДК', 'Родители с детскими колясками'),
        ('ОГД', 'Организованные группы детей'),
        ('ОВ', 'Временно маломобильные'),
        ('ИУ', 'Люди с ментальной инвалидностью'),
    ]
    id_pas = models.AutoField(primary_key=True, verbose_name = 'ID')
    fio_p = models.CharField(max_length=255, verbose_name = 'ФИО Пассажира')
    tep_p = models.CharField(max_length=50, verbose_name = 'Номер телефона')
    sex_p = models.CharField(max_length=10,blank=False, null=False, verbose_name = 'Пол',choices=GENDER_CHOICES)
    pass_category = models.CharField(max_length=50,verbose_name = 'Категория пасажира',choices= CAT_CHOICES)
    dop_inf = models.TextField(blank=True, null=True,verbose_name = 'Дополнительная информация')
    eks = models.BooleanField(verbose_name = 'Наличие кардиостимулятора')

  
    class Meta:
        db_table = 'Passengers'
        verbose_name = 'Пассажира'
        verbose_name_plural = 'Пассажиры'
    
    def __str__(self):
        return self.fio_p
    
    def eks_display(self):
        return 'ДА' if self.eks else 'НЕТ'
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.category = "Пассажиры"	
    #     super(Passengers, self).save(*args, **kwargs)
