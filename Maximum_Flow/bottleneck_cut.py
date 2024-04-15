# Inspiration for pulp package https://blog.sommer-forst.de/2013/04/06/solving-the-minimum-cost-flow-problem-4-pulp/
from pulp import *

graph_edges = {
    (0, 1): 14,
    (0, 1): 25,
    (1, 3): 3,
    (1, 4): 21,
    (2, 3): 13,
    (2, 5): 7,
    (3, 1): 6,
    (3, 5): 15,
    (4, 3): 10,
    (4, 6): 20,
    (5, 4): 5,
    (5, 6): 10
}

source = 0
sink = 6

# prob creates a LP minimization problem
prob = LpProblem("Maximum_Flow", LpMaximize)

# Flow is a dictionary of the flow on each edge
flow = LpVariable.dicts("Flow", graph_edges, lowBound=0, cat=LpInteger)

# Maximizing total flow out of the source node
prob += lpSum(flow[(source, node)] for node in range(len(graph_edges)) if (source, node) in graph_edges)

# Flow conservation constraint
for node in range(1, sink):
    flow_intake = lpSum(flow[(i, node)] for i in range(len(graph_edges)) if (i, node) in graph_edges)
    flow_outtake = lpSum(flow[(node, j)] for j in range(len(graph_edges)) if (node, j) in graph_edges)
    prob += flow_intake - flow_outtake == 0

for edge, capacity in graph_edges.items():
    prob += flow[edge] <= capacity

prob.solve()

bottleneck_cut = [(i, j) for (i, j), cap in graph_edges.items() if value(flow[(i, j)]) == cap]

print("Bottleneck Cut:", bottleneck_cut)

