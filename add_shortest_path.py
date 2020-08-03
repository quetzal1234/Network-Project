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
        '''
        This function adds the nodes (exhibits) in the network from a csv. In this case, the nodes are points of
        interest in the St. Louis Zoo
        :param node_file: csv
        :return: nx network
        '''
        with open(node_file, newline='', encoding='latin-1') as nodes:
            nodereader = csv.reader(nodes, delimiter=',')
            for row in nodereader:
                self.add_node(row[0], fullname=row[1], area=row[2], type=row[-1])

    def add_edge_from_file(self, edge_file):
        '''
        This function adds the edges in the network from a csv. The edges are the paths between the points of
        interest and information about them.
        :param edge_file: csv
        :return: nx network
        '''
        with open(edge_file, newline='') as edges:
            edgereader = csv.reader(edges, delimiter=',')
            for line in edgereader:
                self.add_edge(line[0], line[1], distance=float(line[2]), weight=line[-1])

    def choose_direction(self):
        '''
        This function prompts the user to choose a start and end point for their navigation based on a list of the
        nodes.
        :return: a list of two nodes.
        '''
        while True:
            exhibits = list(self.nodes(data = 'fullname'))
            for exhibit in exhibits:
                print(exhibit[0], ';', exhibit[1])
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
                    return self.directions
                elif start or end in ['quit', 'Quit']:
                    print('All done now, bye!')
                    break  # exit the loop, which will quit the program
                else:
                    print('Unrecognized option! Please try again.')
                    break

    def get_shortest_path(self):
        '''
        Finds shortest path between the user selected nodes and prints it for the user.
        :return: prints to console
        '''
        # d = self.choose_direction()
        if len(self.directions) == 2:
            print('Shortest Path:')
            user_path = nx.algorithms.shortest_path(self, self.directions[0], self.directions[1], weight='distance', method='dijkstra')
            print('Start at')
            for item in user_path:
                print(item, 'go to')
            print('Finish')
        else:
            pass

    def get_shortest_ada_path(self):
        '''
        Finds the shortest path excluding edges that are not ada accessible.
        :return: Prints to console
        '''
        print('ADA option:')
        if len(self.directions) == 2:
            ada_path = nx.dijkstra_path(self, self.directions[0], self.directions[1], weight='weight')
            print('Start at')
            for item in ada_path:
                print(item, 'go to')
            print('Finish')


z = zoodirections()
z.add_node_from_file('node_file.csv')
z.add_edge_from_file('edge_file.csv')
z.choose_direction()
my_path = z.get_shortest_path()
z.get_shortest_ada_path()
