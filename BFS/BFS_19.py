'''
출제 : 백준
난이도 : 레벨 2
문제 : 토마토 (3차원)
날짜 : 21.05.15
유형 : BFS
'''

dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]

from collections import deque

m, n, h = map(int,input().split())
maps = [  [list(map(int,input().split()) ) for _ in range(n) ] for _ in range(h) ]

q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if maps[k][i][j] == 1:
                q.append((k,i,j,0))

ans = 0

while q:
    z, x, y, c = q.popleft()
    ans = c
    for idx in range(6):
        nx = x + dx[idx]
        ny = y + dy[idx]
        nz = z + dz[idx]

        if 0<= nx <n and 0<= ny <m and 0<= nz <h:
            if maps[nz][nx][ny] == 0:
                maps[nz][nx][ny] = 1
                q.append((nz,nx,ny,c+1))

flag = True

for k in range(h):
    for i in range(n):
        for j in range(m):
            if maps[k][i][j] == 0:
                flag = False

if flag:
    print(ans)
else:
    print(-1)

'''
3차원 토마토 오랜만에 풀려고하니깐
헷갈리네 
'''