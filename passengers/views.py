from django.shortcuts import render
from django.http import JsonResponse
from .forms import PassengersForm
from .models import Passengers
from django.contrib.auth.decorators import login_required

@login_required
def add_passenger(request):
    if request.method == 'POST':
        form = PassengersForm(request.POST)
        if form.is_valid():
            passenger = form.save()
            response_data = {
                'id_pas': passenger.id_pas,
                'fio_p': passenger.fio_p,
                'tep_p': passenger.tep_p,
                'sex_p': passenger.sex_p,
                'pass_category': passenger.pass_category,
                'dop_inf': passenger.dop_inf,
                'eks': passenger.eks,
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = PassengersForm()
    
    passengers_list = Passengers.objects.all()
    
    return render(request, 'passengers/passengers.html', {'form': form, 'passengers_list': passengers_list})

def success_view(request):
    return render(request, 'passengers/success.html')
