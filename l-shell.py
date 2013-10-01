import pygraphviz as pgv;

G = pgv.AGraph()



G.add_edge('a','b')
G.add_edge('a','c')
G.add_edge('a','d')
G.add_edge('b','c')
G.add_edge('b','d')
G.add_edge('c','d')

G.add_edge('1','2')
G.add_edge('1','3')
G.add_edge('1','4')
G.add_edge('2','3')
G.add_edge('2','4')
G.add_edge('3','4')

G.add_edge('a','4')

print G
G.write ("l-shell.dot")