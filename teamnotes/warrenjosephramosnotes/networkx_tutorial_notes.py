import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Adds one node at a time
G.add_node(1)

# Adds a list of nodes
G.add_nodes_from([2,5,3,4])

# Generates a graph that connects 10 nodes
H = nx.path_graph(10)

# The Graph G adds nodes that were in Graph H
G.add_nodes_from(H)

# The Graph G adds H as a node
G.add_node(H)

# Adds an edge one at a time
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*

# Adds a list of edges (Does the same thing as lines 21 - 24)
G.add_edges_from([(1, 2), (2, 3)])

# Adds an any ebunch of edges. An ebunch is any iterable container 
# of edge-tuples. An edge-tuple can be a 2-tuple of nodes or a 3-tuple with 2 
# # nodes followed by an edge attribute dictionary, e.g., (2, 3, 
# {'weight': 3.1415})
G.add_edges_from(H.edges)

# Removes all nodes and edges
G.clear()

# add new nodes/edges and NetworkX quietly ignores any that are already present
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

# the graph G consists of 8 nodes and 3 edges, as can be seen by
print(G.number_of_nodes())
print(G.number_of_edges())

# Prints the list of nodes in Graph G
print(list(G.nodes))
# Prints a list of edges in Graph G
print(list(G.edges))
# Prints the list of adjacent nodes to node 1
print(list(G.adj[1]))  # or list(G.neighbors(1))
# Prints the number of edges node 1 has
print(G.degree[1])  # the number of edges incident to 1

# They are also dict-like in that you can look up node and edge data attributes
# via the views and iterate with data attributes using methods .items(), 
# .data('span')
# print(G.items(1))

# One can specify to report the edges and degree from a subset of all 
# nodes using an nbunch. An nbunch is any of: None (meaning all nodes), 
# a node, or an iterable container of nodes that is not itself a node in the graph.
G.edges([2, 'm'])
G.degree([2, 3])

# One can remove nodes and edges from the graph in a similar fashion to 
# adding. Use methods Graph.remove_node(), Graph.remove_nodes_from(), 
# Graph.remove_edge() and Graph.remove_edges_from(), e.g.
G.remove_node(2)
G.remove_nodes_from("spam")
list(G.nodes)
G.remove_edge(1, 3)

G.clear()
H.clear()

# When creating a graph structure by instantiating
# one of the graph classes you can specify data in several formats.
G.add_edge(1, 2)
H = nx.DiGraph(G)   # create a DiGraph using the connections from G
list(H.edges())
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)

# In addition to the views Graph.edges(), and Graph.adj(),
# access to edges and neighbors is possible using subscript notation.
G[1]  # same as G.adj[1]
# Returns AtlasView({2: {}})
G[1][2]
# Returns {}
G.edges[1, 2]
# Returns {}

# You can get/set the attributes of an edge using subscript
# notation if the edge already exists.
G.add_edge(1, 3)
G[1][3]['color'] = "blue"
G.edges[1, 2]['color'] = "red"



# Prints out the name of the graph, the type, num nodes, num edges, and degree
# print(nx.info(G))
# Draws the graph with labels
nx.draw(G, with_labels=True)
# Shows the drawn graph
plt.show()


nx.draw(H, with_labels=True)
plt.show()

