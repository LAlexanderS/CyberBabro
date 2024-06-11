from django import forms
from .models import Shift, Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['last_name', 'first_name', 'second_name', 't_n', 'description', 'uch', 'rank', 'sex', 't_tel', 'r_tel', 'zdo']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            't_n': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'uch': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            't_tel': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'r_tel': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'zdo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['time_work_begin', 'time_work_end', 'date', 'id_insp']
        widgets = {
            'time_work_begin': forms.TimeInput(format='%H:%M', attrs={'class': 'time-input-start'}),
            'time_work_end': forms.TimeInput(format='%H:%M', attrs={'class': 'time-input-end'}),
            'date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'date-input'}),
            'id_insp': forms.Select(attrs={'class': 'form-select'})
        }
        input_formats = {
            'time_work_begin': ['%H:%M'],
            'time_work_end': ['%H:%M'],
            'date': ['%d-%m-%Y'],
        }