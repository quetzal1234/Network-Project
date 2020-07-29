import csv
import networkx as nx

g = nx.DiGraph()
with open('node_file.csv', newline='', encoding = 'latin-1') as csvfile_1:
     reader = csv.reader(csvfile_1, delimiter=',')
     for row in reader:
        print(row)
        g.add_node(row[0], fulname = row[1], area = row[-1])

with open('edge_file.csv', newline='') as csvfile_2:
    reader = csv.reader(csvfile_2, delimiter=',')
    for line in reader:
        g.add_edge(line[0], line[1], distance=line[-1])
