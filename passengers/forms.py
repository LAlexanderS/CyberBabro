from django import forms
from .models import Passengers

class PassengersForm(forms.ModelForm):
    class Meta:
        model = Passengers
        fields = ['fio_p', 'tep_p', 'sex_p', 'pass_category', 'dop_inf', 'eks']
        widgets = {
            'sex_p': forms.Select(choices=Passengers.GENDER_CHOICES, attrs={'class': 'gender-select'}),
            'tep_p': forms.TextInput(attrs={'type': 'tel', 'class': 'mobile-input', 'placeholder': 'Номер телефона'}),
            'dop_inf': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Дополнительная информация'}),
        }
