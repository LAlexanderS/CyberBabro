from django.shortcuts import render, redirect
from .forms import StationForm, StationtimeForm, TransfertimeForm
from django.contrib.auth.decorators import login_required

@login_required
def add_station(request):
    if request.method == 'POST':
        station_form = StationForm(request.POST)
        stationtime_form = StationtimeForm(request.POST)
        transfertime_form = TransfertimeForm(request.POST)
        
        if station_form.is_valid() and stationtime_form.is_valid() and transfertime_form.is_valid():
            station_form.save()
            stationtime_form.save()
            transfertime_form.save()
            return redirect('success')
    else:
        station_form = StationForm()
        stationtime_form = StationtimeForm()
        transfertime_form = TransfertimeForm()
    
    context = {
        'station_form': station_form,
        'stationtime_form': stationtime_form,
        'transfertime_form': transfertime_form,
    }
    return render(request, 'metro/metro.html', context)
