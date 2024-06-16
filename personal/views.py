from django.shortcuts import render
from django.http import JsonResponse

from personal.models import Personal, Shift
from .forms import PersonalForm, ShiftForm
from django.contrib.auth.decorators import login_required

@login_required
def add_personal_and_shift(request):
    if request.method == 'POST':
        if 'personal_form' in request.POST:
            personal_form = PersonalForm(request.POST)
            if personal_form.is_valid():
                personal_form.save()
                return JsonResponse({'success': True})
            else:
                errors = personal_form.errors
                return JsonResponse({'success': False, 'errors': errors}, status=400)

        elif 'shift_form' in request.POST:
            shift_form = ShiftForm(request.POST)
            if shift_form.is_valid():
                shift_form.save()
                return JsonResponse({'success': True})
            else:
                errors = shift_form.errors
                return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        personal_form = PersonalForm()
        shift_form = ShiftForm()
    
    personal_list = Personal.objects.all()
    shift_list = Shift.objects.all()
    
    context = {
        'personal_form': personal_form,
        'shift_form': shift_form,
        'personal_list': personal_list,
        'shift_list': shift_list,
    }
    return render(request, 'personal/personal.html', context)
