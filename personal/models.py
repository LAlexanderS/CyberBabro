from django.db import models

class Personal(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]

    id_personal = models.AutoField(primary_key=True, verbose_name='ID')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отчество')
    t_n = models.CharField(max_length=8, verbose_name='Табельный номер')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    uch = models.CharField(max_length=10, verbose_name='Участок работы')
    rank = models.CharField(max_length=50, verbose_name='Должность')
    sex = models.CharField(max_length=10, verbose_name='Пол', choices=GENDER_CHOICES)
    t_tel = models.CharField(max_length=12, verbose_name='Рабочий телефон')
    r_tel = models.CharField(max_length=12, blank=True, null=True, verbose_name='Личный телефон')
    zdo = models.BooleanField(verbose_name='Может ли сотрудник выполнять тяжелую работу')

    class Meta:
        db_table = 'Personal'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}. {self.second_name[0]}." if self.second_name else f"{self.last_name} {self.first_name[0]}."

    def full_name_initials(self):
        if self.second_name:
            return f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'
        else:
            return f'{self.last_name} {self.first_name[0]}.'
    full_name_initials.short_description = 'Сотрудник'

class Shift(models.Model):
    id_smena = models.AutoField(primary_key=True, verbose_name='ID')
    id_insp = models.ForeignKey(Personal, blank=True, null=True, to_field='id_personal', on_delete=models.CASCADE)
    smena = models.CharField(max_length=5, verbose_name='Смена')
    date = models.DateField(verbose_name='Дата выхода')
    time_work_begin = models.TimeField(verbose_name='Начало рабочего дня')
    time_work_end = models.TimeField(verbose_name='Окончание рабочего дня')

    def __str__(self):
        formatted_date = self.date.strftime('%d.%m.%Y')
        return f'{self.id_insp}  {formatted_date}'

    class Meta:
        db_table = 'Shift'
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
