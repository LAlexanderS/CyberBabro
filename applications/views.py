from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ApplicationForm, ApplicationTransferForm
from .models import Application
from django.contrib.auth.decorators import login_required

@login_required
def add_all_forms(request):
    applications = Application.objects.all()
    
    application_form = ApplicationForm()
    transfer_form = ApplicationTransferForm()

    if request.method == 'POST':
        if 'application_form' in request.POST:
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                return JsonResponse({'success': True, 'form': 'application'})
            else:
                return JsonResponse({'success': False, 'errors': application_form.errors}, status=400)
        
        if 'transfer_form' in request.POST:
            transfer_form = ApplicationTransferForm(request.POST)
            if transfer_form.is_valid():
                transfer_form.save()
                return JsonResponse({'success': True, 'form': 'transfer'})
            else:
                return JsonResponse({'success': False, 'errors': transfer_form.errors}, status=400)

    context = {
        'applications': applications,
        'application_form': application_form,
        'transfer_form': transfer_form,
 
    }
    return render(request, 'applications/applications.html', context)
