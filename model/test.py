import json, sys
import networkx as nx
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append('../model')

import routes, schedule

with open('./subwey.json', 'r') as pointers:
	pointersJs = json.load(pointers)
with open('./switch.json', 'r') as switch:
	switchJs = json.load(switch)
map = pointersJs + switchJs
graph = routes.Routes(map)
print(graph.CalcDistance(65, 87))


#sheduller tests

with open('staffs.json', 'r') as staffs:
	staffsJs = json.load(staffs)
with open('requests.json', 'r') as requests:
	requestsJs = json.load(requests)
data = dict()
data['requests'] = requestsJs
data['staffs'] = staffsJs
sheduler = schedule.Scheduler(data, graph)
print(sheduler.CreateSchedule())
