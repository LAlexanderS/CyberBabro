from django.shortcuts import render, redirect
from .forms import PassengersForm
from django.contrib.auth.decorators import login_required

@login_required
def add_passenger(request):
    if request.method == 'POST':
        form = PassengersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PassengersForm()
    
    return render(request, 'passengers/passengers.html', {'form': form})
