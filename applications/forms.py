from django import forms
from .models import Application, ApplicationTransfer

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'tpz': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'time3': forms.TimeInput(attrs={'type': 'time'}),
            'time4': forms.TimeInput(attrs={'type': 'time'}),
            'TIME_OVER': forms.TimeInput(attrs={'type': 'time'}),
        }

class ApplicationTransferForm(forms.ModelForm):
    class Meta:
        model = ApplicationTransfer
        fields = '__all__'
        widgets = {
            'time_edit': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'time_s': forms.TimeInput(attrs={'type': 'time'}),
            'time_f': forms.TimeInput(attrs={'type': 'time'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
