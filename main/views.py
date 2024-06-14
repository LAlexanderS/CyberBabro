from django.shortcuts import render
from .models import Personalapplication
from model import routes, schedule
from metro.models import Stationtime, Transfertime

def index(request):
    routes = routes.Routes()
    routes.CalcDistance(Stationtime.id_st1, Stationtime.id_st2)
    routes.CreateShortestPath(Transfertime.id1,Transfertime.id2)

    personal_applications = Personalapplication.objects.select_related('person', 'application').all()
    context = {
        'personal_applications': personal_applications
    }
    return render(request, 'main/index.html', context)
