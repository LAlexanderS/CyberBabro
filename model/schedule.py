import datetime

class Scheduler:
	def __init__(self, start, finish, data):
		self.start = start
		self.finish = finish
		self.requests = list()
		self.busy = dict()
		self.free = dict() # сюда заселектить все сотрудников с этих дат
		self.result = dict()

	def CreateSchedule(self, data):
		for el in data:
			self.requests.append((-1, el['datetime'], el['Id']))
			self.requests.append((1, el['datetime'] + el['TIME_OVER'], el['Id']))
		self.requests.sort()
	
	def Algorithm(self, data):
		for request in self.requests:
			if request[0] == -1:
				if len(self.free) != 0:
					for i in range(data[request[2]]['INSP_SEX_M']):
						self.free['MAN']
				else:
					print("NO WAY TO EXECUTE REQUEST")
			else:

