from django.shortcuts import render, redirect
from .forms import PassengersForm

def add_passenger(request):
    if request.method == 'POST':
        form = PassengersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passengers:success')
    else:
        form = PassengersForm()
    
    return render(request, 'passengers/passengers.html', {'form': form})

def success_view(request):
    return render(request, 'passengers/success.html')

