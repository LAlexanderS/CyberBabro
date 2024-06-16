import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Personalapplication
from metro.models import Stationtime, Transfertime
from model.schedule import Scheduler  # Обратите внимание на правильный путь импорта
from model.routes import Routes  # Обратите внимание на правильный путь импорта
from personal.models import Personal
from applications.models import Application
import networkx as nx

def index(request):
    station_times = Stationtime.objects.all().values('id_st1', 'id_st2', 'time')
    transfer_times = Transfertime.objects.all().values('id1', 'id2', 'time')
    id_person = list(Personal.objects.all().values_list('ID', flat=True))
    id_applic = list(Application.objects.all().values_list('id', flat=True))

    if not id_person or not id_applic:
        raise ValueError("Оба списка id_person и id_applic должны содержать данные.")

    combined_list = []
    i, j = 0, 0

    while j < len(id_applic):
        combined_list.append((i + 1, id_person[i % len(id_person)], id_applic[j]))
        i += 1
        j += 1
    
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
        
    routes_instance = Routes(vertexes)
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
        'result': combined_list,
    }
    return render(request, 'main/index.html', context)

@login_required
@require_http_methods(["GET"])
def run_scheduler(request):
    # Сбор данных из моделей
    staffs = list(Personal.objects.all().values())
    requests = list(Application.objects.all().values())
    
    # Сбор данных для графа
    station_times = list(Stationtime.objects.all().values('id_st1', 'id_st2', 'time'))
    transfer_times = list(Transfertime.objects.all().values('id1', 'id2', 'time'))
    
    vertexes = [
        {'id_st1': st['id_st1'], 'id_st2': st['id_st2'], 'time': str(st['time'])} for st in station_times
    ] + [
        {'id1': tr['id1'], 'id2': tr['id2'], 'time': str(tr['time'])} for tr in transfer_times
    ]
    
    # Создание экземпляра маршрутов
    routes_instance = Routes(vertexes)
    
    # Формирование данных для планировщика
    data = {
        'staffs': staffs,
        'requests': requests
    }
    
    # Создание экземпляра планировщика и выполнение расписания
    scheduler = Scheduler(data, routes_instance)
    results = scheduler.CreateSchedule()
    
    # Преобразование результатов в формат JSON для передачи в шаблон
    results_json = json.dumps(results, ensure_ascii=False)
    
    # Передача данных в шаблон
    return render(request, 'main/scheduler_results.html', {'results': results_json})

def distribute_tasks(request):
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
        
    routes_instance = Routes(vertexes)
    distance = None
    shortest_path = None
    
    for record in vertexes:
        if 'id_st1' in record and 'id_st2' in record:
            distance = routes_instance.CalcDistance(int(record['id_st1']), int(record['id_st2']))
        elif 'id1' in record and 'id2' in record:
            shortest_path = routes_instance.CreateShortestPath(int(record['id1']), int(record['id2']))
    
    response_data = {
        'distance': distance,
        'shortest_path': shortest_path
    }
    return JsonResponse(response_data)


