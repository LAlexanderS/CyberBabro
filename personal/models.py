from django.db import models

class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255, verbose_name = 'Фамилия')
    first_name = models.CharField(max_length=255,blank=False,null=False, verbose_name = 'Имя')
    second_name = models.CharField(max_length=255,blank=True, null=True, verbose_name = 'Отчество')
    t_n = models.CharField(max_length=8, verbose_name='Табельный номер сотрудника')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    uch = models.CharField(max_length=10,blank=False,null=False,  verbose_name = 'Участок работы')
    rank = models.CharField(max_length=50,blank=False,null=False, verbose_name = 'Должность')
    sex = models.CharField(max_length=10,blank=False, null=False, verbose_name = 'Пол')
    t_tel = models.CharField(max_length=50, blank=False, null=False, verbose_name = 'Номер рабочего телефона')
    r_tel = models.CharField(max_length=50,blank=True, null=True, verbose_name = 'Номер личного телефона')
    zdo = models.BooleanField(blank=False, verbose_name = 'Может ли сотрудник выполнять тяжелую работу')

    def last_name_with_initials(self):
        initials = f"{self.first_name[0]}. {self.second_name[0]}." if self.second_name else f"{self.first_name[0]}."
        return f"{self.last_name} {initials}"

  
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

class Shift(models.Model):
    id_smena = models.AutoField(primary_key=True)
    #id_insp = models.ForeignKey(Personal, to_field='id_personal', on_delete=models.CASCADE)
    smena = models.IntegerField(verbose_name = 'Смена')
    date = models.DateField(verbose_name = 'Дата выходна')
    time_work_begin = models.TimeField(verbose_name = 'Начало рабочего дня')
    time_work_end = models.TimeField(verbose_name = 'Окончание рабочего дня')

    def __str__(self):
        return f'{self.id_insp} - {self.date}'

    class Meta:
        db_table = 'Shifh'
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.category = "Смены"
        super(Shift, self).save(*args, **kwargs)    

