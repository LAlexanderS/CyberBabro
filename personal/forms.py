from django import forms
from .models import Personal, Shift

# # class TimeRangeWidget(forms.MultiWidget):
#     def __init__(self, attrs=None):
#         widgets = [
#             forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
#             forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
#         ]
#         super().__init__(widgets, attrs)

#     def decompress(self, value):
#         if value:
#             return value.split('-')
#         return [None, None]

#     def format_output(self, rendered_widgets):
#         return '{} - {}'.format(*rendered_widgets)

# class TimeRangeField(forms.MultiValueField):
#     widget = TimeRangeWidget

#     def __init__(self, *args, **kwargs):
#         fields = [
#             forms.TimeField(),
#             forms.TimeField(),
#         ]
#         super().__init__(fields, *args, **kwargs)

#     def compress(self, data_list):
#         if data_list:
#             return '{}-{}'.format(*data_list)
#         return ''

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'last_name', 'first_name', 'second_name', 'UCHASTOK', 'SEX', 'TIME_WORK', 'SMENA', 'RANK', 'DATE', 't_n', 'description', 't_tel', 'r_tel', 'zdo'
        ]
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'UCHASTOK': forms.Select(attrs={'class': 'form-control', 'id': 'uchastok-select'}),
            'SEX': forms.Select(attrs={'class': 'form-control'}),
            'TIME_WORK': forms.Select(attrs={'class': 'form-control', 'id': 'time-work-select'}),
            'SMENA': forms.Select(attrs={'class': 'form-control'}),
            'RANK': forms.Select(attrs={'class': 'form-control'}),
            'DATE': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            't_n': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            't_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'r_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'zdo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        instance = super(PersonalForm, self).save(commit=False)
        first_initial = instance.first_name[0] + '.' if instance.first_name else ''
        second_initial = instance.second_name[0] + '.' if instance.second_name else ''
        instance.FIO = f'{instance.last_name} {first_initial}{second_initial}'.strip()
        if commit:
            instance.save()
        return instance


class ShiftForm(forms.ModelForm):
    id_insp = forms.ModelChoiceField(
        queryset=Personal.objects.all(),
        label="ID Сотрудника",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Shift
        fields = ['id_insp', 'SMENA', 'date', 'time_work_begin']
        widgets = {
            'id_insp': forms.Select(attrs={'class': 'form-control'}),
            'SMENA': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_work_begin': forms.Select(attrs={'class': 'form-control'}),
        }


