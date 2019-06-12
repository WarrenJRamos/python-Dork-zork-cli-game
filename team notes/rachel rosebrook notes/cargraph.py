
import matplotlib.pyplot as plt
import networkx as nx

G.clear()
G = nx.cat_graph()
# explicitly set positions
pos = {0: (1, 1),
       1: (1, 3),
       2: (3, 4.5),
       3: (5, 4.5),
       4: (7, 3), 
       5: (7, 1), 
       6: (6, 0), 
       7: (2, 0),
       8: (1.5, 3.4),
       9: (1.5, 6),
       10: (3.6, 4.5),
       11: (4.4, 4.5),
       12: (6.5, 6),
       13: (6.5, 3.4),
       14: (2.5, 3.5), 
       15: (3.5, 3.5),
       16: (3.5, 2.5),
       17: (2.5, 2.5), 
       18: (3.5, 3),
       19: (3, 3),
       20: (3, 2.5), 
       21: (4.5, 3.5),
       22: (5.5, 3.5),
       23: (5.5, 2.5), 
       24: (4.5, 2.5),
       25: (5.5, 3),
       26: (5, 3),
       27: (5, 2.5),
       28: (4, 2.7),
       29: (3.6, 1.7),
       30: (4.4, 1.7),
       31: (4, 1.7),
       32: (4, 1),
       33: (3, 1),
       34: (2.5, 1.5),
       35: (5, 1),
       36: (5.5, 1.5),
       37: (2.7, 1.9),
       38: (0.2, 1.3),
       39: (0.2, 2.8),
       40: (5.3, 1.9),
       41: (7.8, 1.3),
       42: (7.8, 2.8)}

nx.draw_networkx_nodes(G, pos, node_size=5, nodelist=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], node_color='#808080')
nx.draw_networkx_nodes(G, pos, node_size=5, nodelist=[14, 15, 17, 21, 22, 24], node_color='k')
nx.draw_networkx_nodes(G, pos, node_size=30, nodelist=[16, 18, 19, 20, 23, 25, 26, 27], node_color='g')
nx.draw_networkx_nodes(G, pos, node_size=5, nodelist=[28, 29, 30, 31, 32, 33, 34, 35, 35], node_color='#ffb6c1')
nx.draw_networkx_nodes(G, pos, node_size=1, nodelist=[36, 37, 38, 39, 40, 41, 42], node_color='k')
G.remove_edges_from(G.edges())
G.number_of_edges()
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(7, 0)
G.add_edge(8, 9)
G.add_edge(9, 10)
G.add_edge(11, 12)
G.add_edge(12, 13)
G.add_edge(14, 15)
G.add_edge(15, 16)
G.add_edge(16, 17)
G.add_edge(17, 14)
G.add_edge(21, 22)
G.add_edge(22, 23)
G.add_edge(23, 24)
G.add_edge(24, 21)
G.add_edge(18, 19)
G.add_edge(19, 20)
G.add_edge(25, 26)
G.add_edge(26, 27)
G.add_edge(40, 41)
G.add_edge(40, 42)
G.add_edge(37, 39)
G.add_edge(37, 38)
G.add_edge(28, 29)
G.add_edge(28, 30)
G.add_edge(29, 30)
G.add_edge(31, 32)
G.add_edge(32, 33)
G.add_edge(33, 34)
G.add_edge(32, 35)
G.add_edge(35, 36)


G.number_of_edges()
edges = G.edges()
nx.draw_networkx_edges(G, pos, edge_list=edges)
plt.axis('off')
plt.show()