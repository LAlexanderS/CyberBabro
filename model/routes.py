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
	
	def CalcDistance(self, source, destination):
		try:
			return nx.shortest_path_length(self.graph, source=source, target=destination)
		except nx.NetworkXNoPath:
			return float('inf')
	
	def CreateShortestPath(self, source, destination):
		try:
			return nx.shortest_path(self.graph, source=source, target=destination)
		except nx.NetworkXNoPath:
			return None