from django.shortcuts import render, redirect
from .forms import PersonalForm, ShiftForm

def add_personal_and_shift(request):
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST)
        shift_form = ShiftForm(request.POST)
        if personal_form.is_valid() and shift_form.is_valid():
            personal_form.save()
            shift_form.save()
            return redirect('success')
    else:
        personal_form = PersonalForm()
        shift_form = ShiftForm()
    
    return render(request, 'personal.html', {'personal_form': personal_form, 'shift_form': shift_form})
