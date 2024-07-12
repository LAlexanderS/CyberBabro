import json
import os
import sys
from django.http import JsonResponse
from django.shortcuts import render
from .models import Personalapplication
from metro.models import Stationtime, Transfertime
from model import routes
from personal.models import Personal
from applications.models import Application

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
        
    routes_instance = routes.Routes(vertexes)
    # print(vertexes)
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

sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import routes, schedule


def distribute_tasks(request):
    # Загрузите данные из файлов
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(script_dir, '../model/subwey.json'), 'r', encoding='utf-8') as f:
        pointersJs = json.load(f)
    
    with open(os.path.join(script_dir, '../model/switch.json'), 'r', encoding='utf-8') as f:
        switchJs = json.load(f)
    
    with open(os.path.join(script_dir, '../model/staffs.json'), 'r', encoding='utf-8') as f:
        staffsJs = json.load(f)
    
    with open(os.path.join(script_dir, '../model/requests.json'), 'r', encoding='utf-8') as f:
        requestsJs = json.load(f)
    
    # Объедините данные и выполните вычисления
    map_data = pointersJs + switchJs
    graph = routes.Routes(map_data)
    distance = graph.CalcDistance(65, 87)
    
    data = {
        'requests': requestsJs,
        'staffs': staffsJs
    }
    scheduler = schedule.Scheduler(data, graph)
    schedule_result = scheduler.CreateSchedule()
    
    # Преобразуйте результат в нужный формат
    result = []
    for i, (id_person, id_applic) in enumerate(schedule_result.items(), start=1):
        result.append({'num': i, 'id_person': id_person, 'id_applic': id_applic})
    
    # Верните результат в формате JSON
    return JsonResponse({
        'result': result
    })
