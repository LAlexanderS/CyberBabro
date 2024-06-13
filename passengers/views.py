from django.shortcuts import render, redirect
from .forms import PassengersForm

def add_passenger(request):
    if request.method == 'POST':
        form = PassengersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PassengersForm()
    
    return render(request, 'passengers.html', {'form': form})
