"""
graph={
    "a":["b","c"],
    "b":["a","d"],
  "c":  ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
print(graph)


def DFS(graph, start):
    visited = set()
    stack = [start]

    while stack:#jotokhon pronjonto stack khali hoii loop cholbe
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

DFS(graph, 'A')

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)


graph = {
    '2': ['2', '1', '0'],
    '1': ['3'],
    '0': ['9'],
    '3': [],
    '9': []
}

DFS(graph, '2')


from collections import deque
def BFS(graph, start):
    visited = set()
    stack = deque([start])

    while stack:
        node = stack.popleft()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []

}
BFS(graph, 'A')
"""
from collections import deque

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        visited.add(node)
        print(graph[node]['value'], end=' ')
        for neighbor in graph[node]['next']:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(graph[node]['value'], end=' ')
            queue.extend(graph[node]['next'])

def create_graph():
    return {
        0: {'value': 2, 'next': [1]},
        1: {'value': 2, 'next': [2]},
        2: {'value': 1, 'next': [3]},
        3: {'value': 3, 'next': [4]},
        4: {'value': 1, 'next': [5]},
        5: {'value': 1, 'next': [6]},
        6: {'value': 1, 'next': [7]},
        7: {'value': 5, 'next': [8]},
        8: {'value': 4, 'next': []}
    }

graph = create_graph()

print("DFS:", end=' ')
dfs(graph, 0)

print("\nBFS:", end=' ')
bfs(graph, 0)