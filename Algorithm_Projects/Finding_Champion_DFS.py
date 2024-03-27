def Depth_first_search(graph, node, visited, champions=None, group=None):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            Depth_first_search(graph, neighbor, visited, champions, group)

def Finding_champion_DFS(graph):
    champions = []
    
    for node in graph.keys():
        visited = {node: False for node in graph.keys()}
        Depth_first_search(graph, node, visited, champions)
        if all(visited.values()):
            champions.append(node)
    
    return champions

def divide_into_groups(graph):
    groups = []
    visited = {node: False for node in graph.keys()}
    for node in graph.keys():
        if not visited[node]:
            group = set()
            Depth_first_search(graph, node, visited, group)
            groups.append(group)
    return groups



# Example
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'D': ['B', 'C'],
    'C': ['E', 'F'],
    'E': ['G'],
    'G': ['F'],
    'F': ['E']
}

champions = Finding_champion_DFS(graph)
print("Champions:", champions)
