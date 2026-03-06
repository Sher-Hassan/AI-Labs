import heapq

# 1. Represent the graph (Adjacency List)
graph = {
    'S': {'B_top': 2, 'C': 4, 'B_bot': 4},
    'B_top': {'C': 5, 'G': 5},
    'B_bot': {'C': 1},
    'C': {'G': 3, 'F': 3},
    'G': {'C': 2},
    'F': {'B_bot': 1},
    'E': {'B_bot': 4}
}

# 2. DFS Implementation (Using a Stack)
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded_count = 0
    
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            expanded_count += 1
            if node == goal:
                return path, expanded_count
            visited.add(node)
            for neighbor in reversed(list(graph.get(node, {}).keys())):
                stack.append((neighbor, path + [neighbor]))
    return None, expanded_count

# 2. BFS Implementation (Using a Queue)
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = {start}
    expanded_count = 0
    
    while queue:
        (node, path) = queue.pop(0)
        expanded_count += 1
        if node == goal:
            return path, expanded_count
        
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, expanded_count

# 3. A* Implementation (Using a Priority Queue)
def a_star(graph, start, goal):
    # h(n) = 0 makes it Dijkstra's (Admissible & Consistent)
    def heuristic(n): return 0 
    
    # priority queue: (f_score, current_node, path, g_score)
    pq = [(0 + heuristic(start), start, [start], 0)]
    visited = {} # node: min_g_score
    expanded_count = 0
    
    while pq:
        f, node, path, g = heapq.heappop(pq)
        
        if node in visited and visited[node] <= g:
            continue
            
        visited[node] = g
        expanded_count += 1
        
        if node == goal:
            return path, expanded_count, g
        
        for neighbor, weight in graph.get(node, {}).items():
            new_g = g + weight
            new_f = new_g + heuristic(neighbor)
            heapq.heappush(pq, (new_f, neighbor, path + [neighbor], new_g))
            
    return None, expanded_count, 0

# --- Execution ---
start_node, goal_node = 'S', 'G'

path_dfs, exp_dfs = dfs(graph, start_node, goal_node)
path_bfs, exp_bfs = bfs(graph, start_node, goal_node)
path_ast, exp_ast, cost_ast = a_star(graph, start_node, goal_node)

print(f"DFS: Path: {path_dfs}, Nodes Expanded: {exp_dfs}")
print(f"BFS: Path: {path_bfs}, Nodes Expanded: {exp_bfs}")
print(f"A*:  Path: {path_ast}, Nodes Expanded: {exp_ast}, Total Cost: {cost_ast}")