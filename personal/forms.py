from django import forms
from .models import Personal, Shift

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'FIO', 'UCHASTOK', 'SEX', 'TIME_WORK', 'SMENA', 'RANK', 'DATE',
            'last_name', 'first_name', 'second_name', 't_n', 'description', 't_tel', 'r_tel', 'zdo'
        ]
        widgets = {
            'DATE': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'date-input'}),
            'SEX': forms.Select(choices=Personal.GENDER_CHOICES, attrs={'class': 'gender-select'}),
            't_tel': forms.TextInput(attrs={'type': 'tel', 'class': 'mobile-input', 'placeholder': 'Рабочий телефон'}),
            'r_tel': forms.TextInput(attrs={'type': 'tel', 'class': 'mobile-input', 'placeholder': 'Личный телефон'}),
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['id_insp', 'SMENA', 'date', 'time_work_begin', 'time_work_end']
        widgets = {
            'date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'date-input'}),
            'time_work_begin': forms.TimeInput(format='%H:%M', attrs={'class': 'time-input'}),
            'time_work_end': forms.TimeInput(format='%H:%M', attrs={'class': 'time-input'}),
            'id_insp': forms.Select(attrs={'class': 'form-select'}),
        }
