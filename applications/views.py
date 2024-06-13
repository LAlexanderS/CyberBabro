from django.shortcuts import render, redirect
from .forms import ApplicationForm, ApplicationTransferForm

def add_all_forms(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST, prefix='application')
        application_transfer_form = ApplicationTransferForm(request.POST, prefix='application_transfer')

        if application_form.is_valid() and application_transfer_form.is_valid():
            application_form.save()
            application_transfer_form.save()
            return redirect('add_all_forms')  # Перенаправление после успешной отправки форм
    else:
        application_form = ApplicationForm(prefix='application')
        application_transfer_form = ApplicationTransferForm(prefix='application_transfer')

    context = {
        'application_form': application_form,
        'application_transfer_form': application_transfer_form,
    }

    return render(request, 'applications/applications.html', context)
