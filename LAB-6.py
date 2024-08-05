#LAB 6
#Saliha Batool
#BCS21042


graph = {
    'A': ['B','F','D','E'],
    'B': ['K', 'J'],
    'C': [],
    'D': ['G'],
    'E': ['C','H','I'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['L'],
    'J': [],
    'K': ['N','M'],
    'L':[],
    'M':[],
    'N':[]

}

def dfs(graph, start_node,goal_node):
    visited = set()
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            if node==goal_node:
                return
            # Add all unvisited children to the stack
            for child in reversed(graph[node]):
                if child not in visited:
                    stack.append(child)

# Call DFS with a starting node, e.g., 'A'
dfs(graph,'A','G')
