#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from model import routes


# import networkx as nx

# class Routes:
# 	def __init__(self, vertexes):
# 		self.graph = nx.Graph()
# 		for record in vertexes:
# 			record['time'] = record['time'].replace(',', '.')
# 			if 'id_st1' in record:
# 				self.graph.add_edge(int(record['id_st1']), int(record['id_st2']), weight=float(record['time']))
# 			else:
# 				self.graph.add_edge(int(record['id1']), int(record['id2']), weight=float(record['time']))

# 	def GetGraph(self):
# 		return self.graph
	
# 	#на выходе цифра - растояние между 2 станциями source - id 1 destination id 2
# 	def CalcDistance(self, source, destination):
# 		try:
# 			return nx.shortest_path_length(self.graph, source=source, target=destination)
# 		except nx.NetworkXNoPath:
# 			return float('inf')
	
# 	def CreateShortestPath(self, source, destination):
# 		try:
# 			return nx.shortest_path(self.graph, source=source, target=destination)
# 		except nx.NetworkXNoPath:
# 			return None

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
