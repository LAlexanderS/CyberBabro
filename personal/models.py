from django.db import models

class Personal(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    UCHASTOK_CHOICES = [
        ('ЦУ-1', 'ЦУ-1'),
        ('ЦУ-2', 'ЦУ-2'),
        ('ЦУ-3', 'ЦУ-3'),
        ('ЦУ-3(Н)', 'ЦУ-3(Н)'),
        ('ЦУ-4', 'ЦУ-4'),
        ('ЦУ-4(Н)', 'ЦУ-4(Н)'),
        ('ЦУ-5', 'ЦУ-5'),
        ('ЦУ-8', 'ЦУ-8'),
    ]
    RANK_CHOICES = [
        ('ЦУ', 'Начальник участка'),
        ('ЦСИ', 'Старший инспектор'),
        ('ЦИО', 'Оператор'),
        ('ЦИ', 'Инспектор'),
        ('Администратор', 'Администратор'),
        ('Специалист', 'Специалист'),
    ]
    TIME_WORK_CHOICES = {
        'ЦУ-1': ('7:00 - 19:00', '8:00 - 20:00'),
        'ЦУ-2': ('7:00 - 19:00', '8:00 - 20:00'),
        'ЦУ-3': ('7:00 - 19:00', '8:00 - 20:00', '10:00 - 22:00'),
        'ЦУ-3(Н)': ['20:00 - 8:00'],
        'ЦУ-4': ('7:00 - 19:00', '8:00 - 20:00', '10:00 - 22:00'),
        'ЦУ-4(Н)': ['20:00 - 8:00'],
        'ЦУ-5': ('7:00 - 19:00', '8:00 - 20:00', '10:00 - 22:00'),
        'ЦУ-8': ('7:00 - 19:00', '8:00 - 20:00')
    }
    SMENA_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('1Н', '1Н'),
        ('2Н', '2Н'),
        ('5', '5'),
    ]
    ID = models.AutoField(primary_key=True, verbose_name='ID')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    FIO = models.CharField(max_length=255, verbose_name='ФИО')
    UCHASTOK = models.CharField(max_length=10, blank=True, null=True, verbose_name='Участок работы',choices= UCHASTOK_CHOICES)
    SEX = models.CharField(max_length=10, verbose_name='Пол', choices=GENDER_CHOICES)
    TIME_WORK = models.CharField(max_length=100, verbose_name='Время работы')
    SMENA = models.CharField(max_length=100, verbose_name='Смена',choices= SMENA_CHOICES)
    RANK = models.CharField(max_length=100, verbose_name='Должность', choices=RANK_CHOICES)
    DATE = models.DateField(verbose_name='Дата')
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
        return f'{self.ID}: {self.FIO or f"{self.last_name} {self.first_name} {self.second_name}".strip()}'
    
class Shift(models.Model):
    twb_CHOICES = [
        ('7:00 - 19:00', '7:00 - 19:00'),
        ('8:00 - 20:00', '8:00 - 20:00'),
        ('10:00 - 22:00', '10:00 - 22:00'),
        ('20:00 - 8:00', '20:00 - 8:00'),
    ]

    id_SMENA = models.AutoField(primary_key=True, verbose_name='ID')
    id_insp = models.ForeignKey(Personal, blank=True, null=True, to_field='ID', on_delete=models.CASCADE)
    SMENA = models.CharField(max_length=100, verbose_name='Смена',choices= Personal.SMENA_CHOICES)
    date = models.DateField(verbose_name='Дата выхода')
    time_work_begin =  models.CharField(max_length=50, blank=True, null=True,verbose_name='Время работы',choices= twb_CHOICES)


    class Meta:
        db_table = 'Shift'
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return f'Смена {self.SMENA} - Сотрудник {self.id_insp}'




