import datetime
import heapq
from . import routes

class Scheduler:
	def __init__(self, data):
		self.data = data
		self.requests = list()
		self.busy = dict()
		self.busy['male'] = list()
		self.busy['female'] = list()
		self.free = dict()
		self.free['male'] = list()
		self.free['female'] = list()
		self.free['male_queue'] = list()
		self.free['female_queue'] = list()
		for staff in data['staffs']:
			if staff['SEX'] == 'Мужской':
				self.free['male'].append([0, staff])
			else:
				self.free['female'].append([0, staff])
		self.result = dict()
		self.routes = routes.Routes(data['vertexes'])
		self.lastOrder = dict()

	def CreateSchedule(self):
		for request in self.data['requests']:
			self.requests.append((-1, request['datetime'], request['Id']))
			self.requests.append((1, request['datetime'] + request['TIME_OVER'], request['Id']))
		self.requests.sort()
	
	def Algorithm(self, data):
		for request in self.requests:
			if request[0] == -1:
				if len(self.free) != 0:
					for i in range(data[request[2]]['INSP_SEX_M']):
						self.FindStaff()
				else:
					print("NO WAY TO EXECUTE REQUEST")
			else:
				return 0
		return 0
	
	def CalcDistance(self):
		return 0

	def FindStaff(self, sex, time, stationID):
		if len(self.free[sex]) > 0:
			minCost = self.free[sex][0] + self.routes.CalcDistance()


