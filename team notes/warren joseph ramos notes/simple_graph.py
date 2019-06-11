import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Room 2")
G.add_node("Room 5")

G.add_edge("Room 2", "Room 5")
G.add_edge("Room 4", "Room 1")

G.add_edges_from([("Room 2", "Room 5"), ("Room 1", "Room 3"), ("Room 1","Room 2")])
G.add_edges_from([("Room 6", "Room 4"), ("Room 5", "Room 6")])

print(nx.info(G))

nx.draw(G, with_labels=True)

plt.show()