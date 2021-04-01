'''
출제 : 백준
난이도 : 실버 1
문제 : 미로 탐색
날짜 : 21.01.19
유형 : BFS
'''
from collections import deque
n, m = map(int, input().split())

graph = list( list(map(int,input())) for _ in range(n)  )

d = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q :
        nx, ny = q.popleft()
        for i in d:
            dx = nx + i[0]
            dy = ny + i[1]
            if 0<= dx <n and 0<= dy <m:
                if graph[dx][dy] == 1:
                    graph[dx][dy] += graph[nx][ny]
                    q.append((dx,dy))

bfs(0,0)
print(graph[n-1][m-1])