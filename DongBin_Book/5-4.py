'''
문제 : 미로 탈출
날짜 : 21.04.25
유형 : BFS
'''

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]


def bfs(x, y):

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 :
                    continue
                
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))

'''
5 6
101010
111111
000001
111111
111111
10
'''