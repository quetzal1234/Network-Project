import networkx as nx

class Vertex:
    def __init__(self, key, name, area):
        self.key = key
        self.neighbors = {}
        self.name = name
        self.area = area

    def add_neighbor(self, neighbor, distance=None):
        self.neighbors[neighbor] = distance

    def get_shortestpath(self, key1, key2):
        path = nx.algorithms.shortest_path(self, key1, key2, weight='distance', method='dijkstra')
        print(path)


g = nx.DiGraph()

ver_list = [{'key': "SEN", 'name': "South Entrance", 'area': "Entrance"}, {'key': "BCT", 'name': "Big Cat Country", 'area': "Red Rocks"}, {'key': "PBP", 'name': "Polar Bear Point, Grizzly Ridge", 'area': "The Wild"}, {'key': "SLS", 'name': "Sea Lion Sound", 'area': "Lakeside Crossing"}, {'key': "INS", 'name': "Insectarium", 'area': "Discovery Corner"}, {'key': "RIV", 'name': "River’s Edge", 'area': "River’s Edge"}]
dis_list = [{'key1': "SEN", 'key2': "BCT", 'distance': 10}, {'key1': "SEN", 'key2': "PBP", 'distance': 20}, {'key1': "SEN", 'key2': "BIR", 'distance': 15}, {'key1': "BCT", 'key2': "SLS", 'distance': 15}, {'key1': "BCT", 'key2': "INS", 'distance': 10}, {'key1': "BIR", 'key2': "PBP", 'distance': 20}, {'key1': "BIR", 'key2': "RIV", 'distance': 5}, {'key1': "PBP", 'key2': "SLS", 'distance': 10}, {'key1': "PBP", 'key2': "RIV", 'distance': 15}, {'key1': "INS", 'key2': "RIV", 'distance': 20}]

for i in range(len(ver_list)):
    vertex = Vertex(ver_list[i]['key'], ver_list[i]['name'], ver_list[i]['area'])
    g.add_node(vertex)
    for j in range(len(dis_list)):
        if vertex.key == dis_list[j]['key1']:
            Vertex.add_neighbor(vertex, dis_list[j]['key2'], distance = dis_list[j]['distance'])
            g.add_edge(vertex.key, dis_list[j]['key2'], distance = dis_list[j]['distance'])


Vertex.get_shortestpath(g, "SEN", "INS")
Vertex.get_shortestpath(g, "SEN", "RIV")
Vertex.get_shortestpath(g, "BCT", "RIV")
Vertex.get_shortestpath(g, "SEN", "PBP")
