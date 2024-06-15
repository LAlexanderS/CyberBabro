from django.db import models

class Personal(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    ID = models.AutoField(primary_key=True, verbose_name='ID')
    FIO = models.CharField(max_length=255, verbose_name='ФИО')
    UCHASTOK = models.CharField(max_length=10, blank=True, null=True, verbose_name='Участок работы')
    SEX = models.CharField(max_length=10, verbose_name='Пол', choices=GENDER_CHOICES)
    TIME_WORK = models.CharField(max_length=100, verbose_name='Время работы')
    SMENA = models.CharField(max_length=100, verbose_name='Смена')
    RANK = models.CharField(max_length=100, verbose_name='Должность')
    DATE = models.DateField(verbose_name='Дата')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    t_n = models.CharField(max_length=8, blank=True, null=True, verbose_name='Табельный номер')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    t_tel = models.CharField(max_length=12, blank=True, null=True, verbose_name='Рабочий телефон')
    r_tel = models.CharField(max_length=12, blank=True, null=True, verbose_name='Личный телефон')
    zdo = models.BooleanField(blank=True, null=True, verbose_name='Может ли сотрудник выполнять тяжелую работу')

    class Meta:
        db_table = 'Personal'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    def __str__(self):
        return self.FIO or f'{self.last_name} {self.first_name} {self.second_name}'.strip()    
    

class Shift(models.Model):
    id_SMENA = models.AutoField(primary_key=True, verbose_name='ID')
    id_insp = models.ForeignKey(Personal, blank=True, null=True, to_field='ID', on_delete=models.CASCADE)
    SMENA = models.CharField(max_length=5, verbose_name='Смена')
    date = models.DateField(verbose_name='Дата выхода')
    time_work_begin = models.TimeField(verbose_name='Начало рабочего дня')
    time_work_end = models.TimeField(verbose_name='Окончание рабочего дня')

    class Meta:
        db_table = 'Shift'
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return f'Смена {self.SMENA} - Сотрудник {self.id_insp}' 
