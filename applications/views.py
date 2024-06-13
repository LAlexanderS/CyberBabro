from django.shortcuts import render, redirect
from .forms import ApplicationForm, ApplicationTransferForm

def add_all_forms(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        application_transfer_form = ApplicationTransferForm(request.POST)
        
        if application_form.is_valid() and application_transfer_form.is_valid():
            application_form.save()
            application_transfer_form.save()
            return redirect('success')
    else:
        application_form = ApplicationForm()
        application_transfer_form = ApplicationTransferForm()
    
    context = {
        'application_form': application_form,
        'application_transfer_form': application_transfer_form,
    }
    return render(request, 'applications.html', context)
