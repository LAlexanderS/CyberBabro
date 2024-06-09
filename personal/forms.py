from django import forms
from .models import Shift

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['time_work_begin', 'time_work_end','date','sex','t_tel','r_tel']
        widgets = {
            'time_work_begin': forms.TimeInput(format='%H:%M', attrs={'class': 'time-input-start'}),
            'time_work_end': forms.TimeInput(format='%H:%M', attrs={'class': 'time-input-end'}),
            'date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'date-input'}),
            'sex': forms.Select(attrs={'class': 'gender-select'}),
            'r_tel': forms.TextInput(attrs={'type': 'tel', 'class': 'mobile-input', 'placeholder': 'Введите номер телефона'}),
            't_tel': forms.TextInput(attrs={'type': 'tel', 'class': 'mobile-input', 'placeholder': 'Введите номер телефона'})
        }
        input_formats = {
            'time_work_begin': ['%H:%M'],
            'time_work_end': ['%H:%M'],
            'date': ['%d-%m-%Y'], 
        }