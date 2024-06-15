from django import forms
from .models import Personal, Shift

class TimeRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None, None]

    def format_output(self, rendered_widgets):
        return '{} - {}'.format(*rendered_widgets)

class TimeRangeField(forms.MultiValueField):
    widget = TimeRangeWidget

    def __init__(self, *args, **kwargs):
        fields = [
            forms.TimeField(),
            forms.TimeField(),
        ]
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return '{}-{}'.format(*data_list)
        return ''

class PersonalForm(forms.ModelForm):
    TIME_WORK = TimeRangeField()

    class Meta:
        model = Personal
        fields = [
            'FIO', 'UCHASTOK', 'SEX', 'TIME_WORK', 'SMENA', 'RANK', 'DATE', 'last_name',
            'first_name', 'second_name', 't_n', 'description', 't_tel', 'r_tel', 'zdo'
        ]
        widgets = {
            'FIO': forms.TextInput(attrs={'class': 'form-control'}),
            'UCHASTOK': forms.TextInput(attrs={'class': 'form-control'}),
            'SEX': forms.Select(attrs={'class': 'form-control'}),
            'SMENA': forms.TextInput(attrs={'class': 'form-control'}),
            'RANK': forms.TextInput(attrs={'class': 'form-control'}),
            'DATE': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            't_n': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            't_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'r_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'zdo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['id_insp', 'SMENA', 'date', 'time_work_begin', 'time_work_end']
        widgets = {
            'id_insp': forms.Select(attrs={'class': 'form-control'}),
            'SMENA': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_work_begin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'time_work_end': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
