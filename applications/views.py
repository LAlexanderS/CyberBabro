from django.shortcuts import render, redirect
from .forms import ApplicationForm, ApplicationTransferForm
from model import routes,schedule
from .models import Application

def add_all_forms(request):
    applications = Application.objects.all()
    # routes = routes.Routes()
    # routes.CalcDistance(id1, id2)
    # routes.CreateShortestPath(id,id2)

    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        transfer_form = ApplicationTransferForm(request.POST)
        if application_form.is_valid() and transfer_form.is_valid():
            application_form.save()
            transfer_form.save()
            return redirect('success_page')  # Замените на ваш URL успешной страницы
    else:
        application_form = ApplicationForm()
        transfer_form = ApplicationTransferForm()

    context = {
        "applications": applications,
        'application_form': application_form,
        'transfer_form': transfer_form,
    }
    return render(request, 'applications/applications.html', context)
