from django.shortcuts import render
from .models import Personalapplication
from metro.models import Stationtime, Transfertime
from model import routes
import networkx as nx

def index(request):
    station_times = Stationtime.objects.all().values('id_st1', 'id_st2', 'time')
    transfer_times = Transfertime.objects.all().values('id1', 'id2', 'time')
    
    vertexes = []
    for record in station_times:
        vertexes.append({
            'id_st1': record['id_st1'],
            'id_st2': record['id_st2'],
            'time': str(record['time'])
        })
    for record in transfer_times:
        vertexes.append({
            'id1': record['id1'],
            'id2': record['id2'],
            'time': str(record['time'])
        })
        
    routes_instance = routes.Routes(vertexes)
    print(vertexes)
    distance = None
    shortest_path = None
    
    for record in vertexes:
        try:
            if 'id_st1' in record and 'id_st2' in record:
                distance = routes_instance.CalcDistance(int(record['id_st1']), int(record['id_st2']))
            elif 'id1' in record and 'id2' in record:
                shortest_path = routes_instance.CreateShortestPath(int(record['id1']), int(record['id2']))
        except nx.NetworkXNoPath:
            distance = float('inf')
        except nx.NodeNotFound as e:
            print(f"Ошибка: {e}")

    personal_applications = Personalapplication.objects.select_related('person', 'application').all()
    context = {
        'personal_applications': personal_applications,
        'distance': distance,
        'shortest_path': shortest_path,
    }
    return render(request, 'main/index.html', context)
