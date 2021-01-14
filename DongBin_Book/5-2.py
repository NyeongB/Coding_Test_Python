# 21.01.14
# p.147
# 인접리스트 BFS 예제

from collections import deque

def bfs(graph, v, visited) :
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue :
        v = queue.popleft()
        
        print(v,end=" ")
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9   

bfs(graph, 1, visited)

'''
1 2 7 6 8 3 4 5 
'''
