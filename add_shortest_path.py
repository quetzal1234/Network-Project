import csv
import networkx as nx


class zoodirections(nx.DiGraph):
    def __init__(self):
        super(nx.DiGraph, self).__init__()
        # self.nodes = g.nodes
        self.directions = []
        self._pred = self.adjlist_outer_dict_factory()  # predecessor
        self._succ = self._adj  # successor

    def add_node_from_file(self, node_file):
        with open(node_file, newline='', encoding='latin-1') as nodes:
            nodereader = csv.reader(nodes, delimiter=',')
            for row in nodereader:
                self.add_node(row[0], fullname=row[1], area=row[2], type=row[-1])

    def add_edge_from_file(self, edge_file):
        with open(edge_file, newline='') as edges:
            edgereader = csv.reader(edges, delimiter=',')
            for line in edgereader:
                self.add_edge(line[0], line[1], distance=float(line[2]), bidirectional=line[3], weight=line[-1])

    def choose_direction(self):
        while True:
            print(list(self.nodes))
            print('Please select your start point and destination.')
            print('If you wish to quit, type Quit.')
            start = input('Type the three letter abbreviations of your start point: ')
            if len(start) != 3:  # check prevents a crash
                continue
            end = input('Type the three letter abbreviation of your end point: ')
            if len(end) != 3:  # check prevents a crash
                continue
            else:
                directions = []
                if len(start) + len(end) == 6:
                    directions.append(start.upper())
                    directions.append(end.upper())
                    # return directions
                    self.directions = directions
                if start or end in ['quit', 'Quit']:
                    print('All done now, bye!')
                    break  # exit the loop, which will quit the program
                else:
                    print('Unrecognized option! Please try again.')
                    break

    def get_shortest_path(self):
        # d = self.choose_direction()
        if len(self.directions) == 2:
            user_path = nx.algorithms.shortest_path(self, self.directions[0], self.directions[1], weight='distance', method='dijkstra')
            return user_path
        else:
            False

z = zoodirections()
z.add_node_from_file('node_file.csv')
z.add_edge_from_file('edge_file.csv')
z.choose_direction()
my_path = z.get_shortest_path()
print(my_path)
