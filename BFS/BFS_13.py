'''
출제 : 백준
난이도 : 실버 1
문제 : 토마토 (3차원)
날짜 : 21.04.27
유형 : BFS
'''
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m, n, h = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 1:
                q.append((k,i,j,0))

ans = 0


while q:
    z, x, y, c = q.popleft()
    ans = c
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = 1
                q.append((nz,nx,ny,c+1))

flag = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j] == 0:
                flag = 1
                break

if flag == 0:
    print(ans)
else:
    print(-1)

'''
3차원 배열에 bfs를 구현해야하는 문제
앞으로 3차원은 그냥 외운다
arr[z][x][y]
이렇게 생각하고 문제를 접근한다.
'''