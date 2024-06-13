from django.shortcuts import render, redirect
from .forms import LineForm, StationForm, StationtimeForm, TransfertimeForm, PersonalForm, ShiftForm

def add_all_forms(request):
    if request.method == 'POST':
        line_form = LineForm(request.POST, prefix='line')
        station_form = StationForm(request.POST, prefix='station')
        stationtime_form = StationtimeForm(request.POST, prefix='stationtime')
        transfertime_form = TransfertimeForm(request.POST, prefix='transfertime')
        personal_form = PersonalForm(request.POST, prefix='personal')
        shift_form = ShiftForm(request.POST, prefix='shift')

        if line_form.is_valid() and station_form.is_valid() and stationtime_form.is_valid() and transfertime_form.is_valid() and personal_form.is_valid() and shift_form.is_valid():
            line_form.save()
            station_form.save()
            stationtime_form.save()
            transfertime_form.save()
            personal_form.save()
            shift_form.save()
            return redirect('add_all_forms')  # Перенаправление после успешной отправки форм
    else:
        line_form = LineForm(prefix='line')
        station_form = StationForm(prefix='station')
        stationtime_form = StationtimeForm(prefix='stationtime')
        transfertime_form = TransfertimeForm(prefix='transfertime')
        personal_form = PersonalForm(prefix='personal')
        shift_form = ShiftForm(prefix='shift')

    context = {
        'line_form': line_form,
        'station_form': station_form,
        'stationtime_form': stationtime_form,
        'transfertime_form': transfertime_form,
        'personal_form': personal_form,
        'shift_form': shift_form,
    }

    return render(request, 'metro/metro.html', context)
