import networkx as nx

class Routes:
	def __init__(self, vertexes):
		self.graph = nx.Graph()
		for record in vertexes:
			record['time'] = record['time'].replace(',', '.')
			if 'id_st1' in record:
				self.graph.add_edge(int(record['id_st1']), int(record['id_st2']), weight=float(record['time']))
			else:
				self.graph.add_edge(int(record['id1']), int(record['id2']), weight=float(record['time']))

	def GetGraph(self):
		return self.graph
	
	#на выходе цифра - растояние между 2 станциями source - id 1 destination id 2
	def CalcDistance(self, source, destination):
		if (path := self.CreateShortestPath(source, destination)) != None:
			result = 0
			for i in range(len(path) - 1):
				result += self.graph.get_edge_data(path[i], path[i + 1])['weight']
			return result
		return None
	
	def CreateShortestPath(self, source, destination):
		try:
			return nx.shortest_path(self.graph, source=source, target=destination, weight='string')
		except nx.NetworkXNoPath:
			return None