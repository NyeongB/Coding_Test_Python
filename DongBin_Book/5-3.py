'''
문제 : 음료수 얼려 먹기
날짜 : 21.04.15
유형 : BFS
'''

from collections import deque


graph = []

n, m = map(int, input().split())
d = [(1,0),(-1,0),(0,-1),(0,1)]
def bfs(x,y):
    graph[x][y] = 1

    q = deque()
    q.append((x,y))

    while q:
        t_x,t_y = q.popleft()
        for i in range(4):
            dx = t_x + d[i][0]
            dy = t_y + d[i][1]

            if 0<= dx < len(graph) and 0<= dy < len(graph[0]):
                if graph[dx][dy] == 0:
                    q.append((dx,dy))
                    graph[dx][dy] = 1


for _ in range(n):
    graph.append(list(map(int, input())))


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt +=1
            bfs(i,j)

print(cnt)