from django import forms
from .models import Passengers

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passengers
        fields = ['fio_p', 'tep_p', 'sex_p', 'pass_category', 'dop_inf', 'eks']
        widgets = {
            'fio_p': forms.TextInput(attrs={'class': 'form-control'}),
            'tep_p': forms.TextInput(attrs={'class': 'form-control'}),
            'sex_p': forms.Select(attrs={'class': 'form-control'}),
            'pass_category': forms.TextInput(attrs={'class': 'form-control'}),
            'dop_inf': forms.Textarea(attrs={'class': 'form-control'}),
            'eks': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
