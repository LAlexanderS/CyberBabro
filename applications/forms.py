from django import forms
from .models import Application, ApplicationTransfer

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['id_pas', 'datetime', 'in_p', 'out_p', 'tpz', 'insp_sex_m', 'insp_sex_f', 'time_over', 'id_st1', 'id_st2', 'status', 'vokzal', 'dop_inf', 'bag_s', 'pass_count', 'method_p']
        widgets = {
            'id_pas': forms.Select(attrs={'class': 'form-control'}),
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'in_p': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'out_p': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'tpz': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'insp_sex_m': forms.NumberInput(attrs={'class': 'form-control'}),
            'insp_sex_f': forms.NumberInput(attrs={'class': 'form-control'}),
            'time_over': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'id_st1': forms.Select(attrs={'class': 'form-control'}),
            'id_st2': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'vokzal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dop_inf': forms.Textarea(attrs={'class': 'form-control'}),
            'bag_s': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pass_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'method_p': forms.TextInput(attrs={'class': 'form-control'})
        }

class ApplicationTransferForm(forms.ModelForm):
    class Meta:
        model = ApplicationTransfer
        fields = ['id_bid', 'time_edit', 'time_s', 'time_f']
        widgets = {
            'id_bid': forms.Select(attrs={'class': 'form-control'}),
            'time_edit': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'time_s': forms.Select(attrs={'class': 'form-control'}),
            'time_f': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
