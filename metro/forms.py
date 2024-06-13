from django import forms
from .models import Station, Stationtime, Transfertime

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name_station', 'id_line', 'name_line']
        widgets = {
            'name_station': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название станции'}),
            'id_line': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID линии'}),
            'name_line': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Линия метро'}),
        }

class StationtimeForm(forms.ModelForm):
    class Meta:
        model = Stationtime
        fields = ['time', 'id_st1', 'id_st2']
        widgets = {
            'time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Время в пути'}),
            'id_st1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Станция 1'}),
            'id_st2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Станция 2'}),
        }

class TransfertimeForm(forms.ModelForm):
    class Meta:
        model = Transfertime
        fields = ['time', 'id1', 'id2']
        widgets = {
            'time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Время в пути'}),
            'id1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Станция 1'}),
            'id2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Станция 2'}),
        }
