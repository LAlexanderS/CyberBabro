from django.shortcuts import render, redirect
from .forms import PassengerForm

def add_passenger(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passengers:passengers')
    else:
        form = PassengerForm()
    
    context = {
    "title": "Пассажиры",
    'form': form,
		
	}
    return render(request, 'passengers/passengers.html', context)
