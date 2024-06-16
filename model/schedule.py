import routes

# male female в passengers and personal 
# SEX in applications and personal
#sex_p in passengers
#datetime in applications
#TIME_OVER in applications
#INSP_SEX_M in applications
class Scheduler:
	def __init__(self, data, graph):
		self.data = data
		self.requests = list()
		self.busy = dict()
		self.busy['male'] = list()
		self.busy['female'] = list()
		self.free = dict()
		self.free['male'] = list()
		self.free['female'] = list()
		self.staffs = dict()
		for staff in data['staffs']:
			self.staffs[int(staff['ID'])] = staff
		for staff in data['staffs']:
			if staff['SEX'] == 'Мужской':
				self.free['male'].append(self.staffs[int(staff['ID'])])
			else:
				self.free['female'].append(self.staffs[int(staff['ID'])])
		self.results = dict()
		self.graph = graph
		self.lastOrder = dict()
		self.ordersAmount = dict()
		self.reqDict = dict()

	def CalcCost(self, stuff, dest):
		if int(stuff['ID']) in self.lastOrder:
			return self.ordersAmount[int(stuff['ID'])] + self.graph.CalcDistance(int(self.lastOrder[int(stuff['ID'])]), int(dest))
		return self.ordersAmount.get(int(stuff['ID']), 0)
	
	def CreateSchedule(self):
		for request in self.data['requests']:
			start = self.TranslateTime(request['datetime'][11::])
			end = start + self.TranslateTime(request['TIME_OVER'])
			self.requests.append((start, -1, request['id']))
			self.requests.append((end, 1, request['id']))
			self.reqDict[request['id']] = request
		self.requests.sort()
		self.Algorithm()
		return self.results
		
	
	def Algorithm(self):
		for request in self.requests:
			if request[1] == -1:
				results = list()
				isCan = True
				if len(self.free) != 0:
					man_amount = int(self.reqDict[request[2]]['INSP_SEX_M'])
					woman_amount = int(self.reqDict[request[2]]['INSP_SEX_F'])
					for i in range(man_amount):
						staff_first = self.FindStaff('male', self.reqDict[request[2]]['id_st1'])
						if staff_first == None:
							isCan = False
							break
						else:
							staff = self.staffs[int(staff_first['ID'])]
							results.append(staff)
							self.free['male'].remove(staff)
							self.busy['male'].append(staff)

					for i in range(woman_amount):
						staff_first = self.FindStaff('female', self.reqDict[request[2]]['id_st1'])
						if staff_first == None:
							isCan = False
							break
						else:
							staff = self.staffs[int(staff_first['ID'])]
							results.append(staff)
							self.free['female'].remove(staff)
							self.busy['female'].append(staff)
					
					if isCan:
						for staff in results:
							self.results[int(request[2])] = int(staff['ID'])
							self.lastOrder[int(staff['ID'])] = int(self.reqDict[request[2]]['id_st2'])
							if int(staff['ID']) in self.ordersAmount:
								self.ordersAmount[int(staff['ID'])] += 1
							else:
								self.ordersAmount[int(staff['ID'])] = 1
					else:
						self.results[int(request[2])] = 'NO WAY TO EXECUTE REQUEST'
						for staff in results:
							if staff['SEX'] == 'Мужской':
								self.free['male'].append(staff)
								self.busy['male'].remove(staff)
							else:
								self.free['female'].append(staff)
								self.busy['female'].remove(staff)
				else:
					self.result[request[2]] = 'NO WAY TO EXECUTE REQUEST'
			else:
				if self.results[int(request[2])] != 'NO WAY TO EXECUTE REQUEST':
					staff_id = self.results[int(request[2])]
					if self.staffs[self.results[int(request[2])]]['SEX'] == 'Мужской':
						self.free['male'].append(self.staffs[staff_id])
						self.busy['male'].remove(self.staffs[staff_id])
					else:
						self.free['female'].append(self.staffs[staff_id])
						self.busy['female'].remove(self.staffs[staff_id])

	def FindStaff(self, sex, dest):
		if len(self.free[sex]) > 0:
			min = self.CalcCost(self.free[sex][0], dest)
			staff = self.free[sex][0]
			for i in range(1, len(self.free[sex])):
				cost = self.CalcCost(self.free[sex][i], dest)
				if min > cost:
					staff = self.free[sex][i]
					min = cost
			return staff
		return None

	def TranslateTime(self, time):
		time = time.split(':')
		return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])