import csv
import networkx as nx

#importing csv
g = nx.DiGraph()
with open('node_file.csv', newline='', encoding = 'latin-1') as csvfile_1:
     reader = csv.reader(csvfile_1, delimiter=',')
     for row in reader:
        g.add_node(row[0], fullname = row[1], area = row[2], type = row[-1])

with open('edge_file.csv', newline='') as csvfile_2:
    reader = csv.reader(csvfile_2, delimiter=',')
    for line in reader:
        g.add_edge(line[0], line[1], distance=line[2], bidirectional = line[3], weight=line[-1])


class zoodirections(nx.DiGraph()):
    def __init__(self):
        super(nx.DiGraph(), self).__init__(g)
        self.nodes = g.nodes
    def choose_direction(self):
        while True:
            print(list(self.nodes))
            print('Please select your start point and destination.')
            print('If you wish to quit type Quit.')
            start = input('Type the three letter abbreviations of your start point: ')
            if len(start) == 3: #check prevents a crash
                continue
            end = input('Type the three letter abbreviation of your end point: ')
            if len(end) == 3: #check prevents a crash
                continue
            else:
                directions = []
                if len(start) + len(end) == 6:
                    directions.append(start.upper())
                    directions.append(end.upper())
                    return directions
                if start or end in ['quit', 'Quit']:
                    print('All done now, bye!')
                    break #exit the loop, which will quit the program
                else:
                    print('Unrecognized option! Please try again.')
                    break
