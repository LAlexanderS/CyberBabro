from django import forms
from .models import Appication

class AppicationForm(forms.ModelForm):
    class Meta:
        model = Appication
        fields = '__all__'
        widgets = {
           'vokzal': forms.RadioSelect(choices=[(True, 'ДА'), (False, 'НЕТ')])
        }

						
