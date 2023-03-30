from collections import  deque
graph = {
    1:[2,3],
    2:[4,5],
    3:[6],
    4:[],
    5:[6],
    6:[]
}
start = 1
queue = deque([start])
visited = []
while queue:
    vertex = queue.popleft()
    if vertex not in visited:
        visited.append(vertex)
        queue.extend(graph[vertex])
print(visited)
