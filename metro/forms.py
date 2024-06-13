from django import forms
from .models import Line, Station, Stationtime, Transfertime
from personal.models import Shift, Personal

class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = ['name_line']
        widgets = {
            'name_line': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name_station', 'line']
        widgets = {
            'name_station': forms.TextInput(attrs={'class': 'form-control'}),
            'line': forms.Select(attrs={'class': 'form-control'}),
        }

class StationtimeForm(forms.ModelForm):
    class Meta:
        model = Stationtime
        fields = ['st_1', 'st_2', 'st_time']
        widgets = {
            'st_1': forms.Select(attrs={'class': 'form-control'}),
            'st_2': forms.Select(attrs={'class': 'form-control'}),
            'st_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TransfertimeForm(forms.ModelForm):
    class Meta:
        model = Transfertime
        fields = ['tr_1', 'tr_2', 'transfer_time']
        widgets = {
            'tr_1': forms.Select(attrs={'class': 'form-control'}),
            'tr_2': forms.Select(attrs={'class': 'form-control'}),
            'transfer_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }

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
            'sex': forms.Select(attrs={'class': 'gender-select'}),
            't_tel': forms.TextInput(attrs={'class': 'mobile-input', 'type': 'tel', 'placeholder': 'Введите номер телефона'}),
            'r_tel': forms.TextInput(attrs={'class': 'mobile-input', 'type': 'tel', 'placeholder': 'Введите номер телефона'}),
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
