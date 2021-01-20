# 21.01.20
# p.154
# 미로 탈출

from collections import deque

n,m = map(int,input().split())
graph = []

dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,input())))


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    
    while queue :
        x, y = queue.popleft()  # 이렇게 바로 뽑아버리네
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx<0 or nx>=n or ny <0 or ny>=m:
                continue
            if graph[nx][ny] ==0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])

    
    return graph[n-1][m-1]


print(bfs(0,0))