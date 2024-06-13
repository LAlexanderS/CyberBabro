from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.shortcuts import render, redirect
from .forms import PersonalForm, ShiftForm

def index(request):
  return render(request, 'personal/personal.html')

def add_personal_and_shift(request):
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST, prefix='personal')
        shift_form = ShiftForm(request.POST, prefix='shift')
        if personal_form.is_valid() and shift_form.is_valid():
            personal_form.save()
            shift_form.save()
            return redirect('personal:personal')  # Перенаправление после успешной отправки форм
    else:
        personal_form = PersonalForm(prefix='personal')
        shift_form = ShiftForm(prefix='shift')

    context = {
        'personal_form': personal_form, 
        'shift_form': shift_form
        }



    return render(request, 'personal/personal.html', context)

