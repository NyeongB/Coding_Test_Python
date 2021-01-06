'''
출제 : 백준
난이도 : 실버 2
문제 : DFS와 BFS
날짜 : 21.01.06
유형 : BFS, DFS
'''
from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v) :
    visited[v] = True
    print(v,end=" ")
    for i in range(1, N + 1) :
        if graph[v][i] == 1 and visited[i] == False :
            dfs(i) 

def bfs(v) :
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue :
        temp = queue.popleft()
        print(temp, end=" ")
        for i in range(1, N + 1):
            if graph[temp][i] == 1 and visited[i] == False :
                queue.append(i)
                visited[i] = True
    

dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)