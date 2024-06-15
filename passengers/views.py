from django.shortcuts import render
from django.http import JsonResponse
from .forms import PassengersForm
from django.contrib.auth.decorators import login_required

@login_required
def add_passenger(request):
    if request.method == 'POST':
        form = PassengersForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = PassengersForm()
    
    return render(request, 'passengers/passengers.html', {'form': form})

def success_view(request):
    return render(request, 'passengers/success.html')

