from django.db import models

class Personal(models.Model):
    MALE = 'Мужской'
    FEMALE = 'Женский'
    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    ]
    ID = models.AutoField(primary_key=True, verbose_name = 'ID')
    FIO =  models.CharField(max_length=255, verbose_name = 'ФИО')
    UCHASTOK = models.CharField(max_length=10,blank=True,null=True,  verbose_name = 'Участок работы')
    SEX =  models.CharField(max_length=10,verbose_name = 'Пол')
    TIME_WORK = models.CharField(max_length=100,verbose_name = 'Пол')
    SMENA = models.CharField(max_length=100,verbose_name = 'Смена')
    RANK = models.CharField(max_length=100,verbose_name = 'Должность')
    DATE = models.DateField(verbose_name = 'Дата')
    last_name = models.CharField(max_length=255, verbose_name = 'Фамилия',blank=True,null=True)
    first_name = models.CharField(max_length=255, verbose_name = 'Имя',blank=True,null=True)
    second_name = models.CharField(max_length=255,blank=True, null=True, verbose_name = 'Отчество')
    t_n = models.CharField(max_length=8,blank=True, null=True, verbose_name='Табельный номер')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    t_tel = models.CharField(max_length=12,blank=True, null=True, verbose_name = 'Рабочий телефон')
    r_tel = models.CharField(max_length=12,blank=True, null=True, verbose_name = 'Личный телефон')
    zdo = models.BooleanField(blank=True,null=True, verbose_name = 'Может ли сотрудник выполнять тяжелую работу')


    class Meta:
        db_table = 'Personal'
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    # def __str__(self):
        # return f"{self.last_name} {self.first_name[0]}. {self.second_name[0]}." if self.second_name else f"{self.last_name} {self.first_name[0]}."

    # def full_name_initials(self):
        # if self.second_name:
            # return f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'
        # else:
            # return f'{self.last_name} {self.first_name[0]}.'
    # full_name_initials.short_description = 'Сотрудник'

  
    # def __str__(self):
    #     return self.name
    
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.category = "Сотрудники"
    #     super(Personal, self).save(*args, **kwargs)

class Shift(models.Model):
    id_SMENA = models.AutoField(primary_key=True, verbose_name = 'ID')
    id_insp = models.ForeignKey(Personal,blank=True, null=True, to_field='ID', on_delete=models.CASCADE)
    SMENA = models.CharField(max_length= 5, verbose_name = 'Смена')
    date = models.DateField(verbose_name = 'Дата выхода')
    time_work_begin = models.TimeField(verbose_name = 'Начало рабочего дня')
    time_work_end = models.TimeField(verbose_name = 'Окончание рабочего дня')

    def __str__(self):
        formatted_date = self.date.strftime('%d.%m.%Y')
        return f'{self.id_insp}  {formatted_date}'

    class Meta:
        db_table = 'Shift'
        verbose_name = 'Смену'
        verbose_name_plural = 'Смены'

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.category = "Смены"
    #     super(Shift, self).save(*args, **kwargs)    

