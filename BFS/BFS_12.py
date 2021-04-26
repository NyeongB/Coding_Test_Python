'''
출제 : 백준
난이도 : 실버 1
문제 : 토마토 (2차원)
날짜 : 21.04.26
유형 : BFS
'''
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n, = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j,0))

def bfs():
    result = 0
    while q:
        x, y, count = q.popleft()
        result = count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    q.append((nx, ny, count + 1))

    return result


flag = 0
ans = bfs()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = 1
            break
if flag == 1:
    print(-1)
else:
    print(ans)