import csv
import networkx as nx


class zoodirections(nx.DiGraph):
    def __init__(self):
        super(nx.DiGraph, self).__init__()
        # self.nodes = g.nodes
        self.directions = []
        self._pred = self.adjlist_outer_dict_factory()  # predecessor
        self._succ = self._adj  # successor
        self.startval = ''
        self.endval = ''

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
                self.add_edge(line[0], line[1], distance=float(line[2]), weight=float(line[-1]))

    def choose_direction(self):
        '''
        This function prompts the user to choose a start and end point for their navigation based on a list of the
        nodes.
        :return: a list of two nodes.
        '''
        while True:
            exhibits = list(self.nodes(data = 'fullname'))
            exhibits = sorted(exhibits)
            accum = 0
            for exhibit in exhibits:
                accum = accum + 1
                print(accum,".", exhibit[0],';', exhibit[1])
            print('Please select your start point and destination.')
            print('If you wish to quit, type Quit.')
            if(self.endval):
                inputstr = 'Type the three letter abbreviations of your start point. Default:' + self.endval + ':'
            else:
                inputstr = 'Type the three letter abbreviations of your start point:'
            start = input(inputstr)
            if len(start) < 1:
                start = self.endval
                print('Using ' + self.endval + ' as starting point')
            if start in ['quit', 'Quit']:
                print('All done now, bye!')
                break  # exit the loop, which will quit the program
            if len(start) != 3:  # check prevents a crash
                continue
            end = input('Type the three letter abbreviation of your end point: ')
            if end in ['quit', 'Quit']:
                print('All done now, bye!')
                break  # exit the loop, which will quit the program
            self.endval = end.upper()
            if len(end) != 3:  # check prevents a crash
                continue
            else:
                directions = []
                if len(start) + len(end) == 6:
                    directions.append(start.upper())
                    directions.append(end.upper())
                    # return directions
                    self.directions = directions
                    # return self.directions
                    self.get_shortest_path()
                    self.get_shortest_ada_path()
                    continue
                #elif start or end in ['quit', 'Quit']:
                #    print('All done now, bye!')
                #    break  # exit the loop, which will quit the program
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
                print(self.nodes[item]['fullname'], 'go to')
                # this is where we need to calculate the distance
            print('Finish')
            print('Total distance:')
            print(nx.shortest_path_length(self, source=self.directions[0], target=self.directions[1], weight='distance'))
        else:
            pass

    @staticmethod
    def accessible_weight(u,v,d):
        '''
        Adjusts the weights for the ADA path.
        :param u:
        :param v:
        :param d:
        :return: edge_dist: distances weighted by accessibility
        '''
        edge_dist = d.get('distance')
        edge_wt = d.get('weight', 1)
        if edge_wt == 0:
            return edge_dist
        else:
            return edge_dist * 1000

    def get_shortest_ada_path(self):
        '''
        Finds the shortest path excluding edges that are not ada accessible.
        :return: Prints to console
        '''
        print('ADA option:')
        if len(self.directions) == 2:
            ada_path = nx.dijkstra_path(self, self.directions[0], self.directions[1], weight= zoodirections.accessible_weight)
            print('Start at')
            for item in ada_path:
                print(self.nodes[item]['fullname'], 'go to')
                # this is where we need to calculate the distance
            print('Finish')
            print('Total distance:')
            print(nx.shortest_path_length(self, source=self.directions[0], target=self.directions[1], weight=zoodirections.accessible_weight))
        else:
            pass

z = zoodirections()
z.add_node_from_file('node_file.csv')
z.add_edge_from_file('edge_file.csv')
z.choose_direction()
# my_path = z.get_shortest_path()
# z.get_shortest_ada_path()
