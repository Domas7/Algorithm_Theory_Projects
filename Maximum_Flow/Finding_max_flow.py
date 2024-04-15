# Inspiration from https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.maximum_flow.html
import networkx as nx

G = nx.DiGraph()
G.add_edge(0, 1, capacity=14)
G.add_edge(0, 1, capacity=25)
G.add_edge(1, 3, capacity=3)
G.add_edge(1, 4, capacity=21)
G.add_edge(2, 3, capacity=13)
G.add_edge(2, 5, capacity=7)
G.add_edge(3, 1, capacity=6)
G.add_edge(3, 5, capacity=15)
G.add_edge(4, 3, capacity=10)
G.add_edge(4, 6, capacity=20)
G.add_edge(5, 4, capacity=5)
G.add_edge(5, 6, capacity=10)


flow_value, flow_dict = nx.maximum_flow(G, 0, 6)

print("Maximum Flow Value:", flow_value)
print("Flow through each edge:", flow_dict)

for u, neighboors in flow_dict.items():
    for v, flow in neighboors.items():
        if flow > 0:
            print(f"Flow from {u} to {v} is {flow}")