from django import forms
from .models import Application, ApplicationTransfer

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'id_pas', 'datetime', 'tpz', 'time3', 'time4', 'INSP_SEX_M', 'INSP_SEX_F',
            'TIME_OVER', 'cat_pas', 'id_st1', 'id_st2', 'status', 'vokzal', 'dop_inf',
            'bag_s', 'pass_count', 'method_p'
        ]
        widgets = {
            'id_pas': forms.Select(attrs={'class': 'form-control'}),
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'tpz': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'time3': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'time4': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'INSP_SEX_M': forms.NumberInput(attrs={'class': 'form-control'}),
            'INSP_SEX_F': forms.NumberInput(attrs={'class': 'form-control'}),
            'TIME_OVER': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'cat_pas': forms.TextInput(attrs={'class': 'form-control'}),
            'id_st1': forms.TextInput(attrs={'class': 'form-control'}),
            'id_st2': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'vokzal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dop_inf': forms.Textarea(attrs={'class': 'form-control'}),
            'bag_s': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pass_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'method_p': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ApplicationTransferForm(forms.ModelForm):
    class Meta:
        model = ApplicationTransfer
        fields = ['id_bid', 'time_edit', 'time_s', 'time_f', 'date_time']
        widgets = {
            'id_bid': forms.TextInput(attrs={'class': 'form-control'}),
            'time_edit': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'time_s': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'time_f': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
