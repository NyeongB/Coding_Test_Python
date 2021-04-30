'''
출제 : 백준
난이도 : 골드 5
문제 : 직사각형 탈출
날짜 : 21.04.30
유형 : BFS
'''
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

h, w, sr, sc, fr, fc = map(int, input().split())
visited = set()

# 충돌 검사
def check(x,y):

    for i in range(h):
        for j in range(w):
            nx = x + i
            ny = y + j
            if not(0 <= nx < n and 0 <= ny < m):
                visited.add((nx,ny))
                return False
            if arr[nx][ny] == 1:
                visited.add((nx,ny))
                return False

    return True

q = deque()

q.append((sr-1,sc-1,0))

visited.add((sr-1,sc-1))
x, y, d = (0,0,0)
while q:
    x, y, d = q.popleft()
    if x == (fr-1) and y == (fc-1):
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and check(nx,ny):
            if (nx,ny) not in visited:
                if arr[nx][ny] ==0:
                    q.append((nx,ny,d+1))
                    visited.add((nx,ny))

#print(visited)
if x == fr - 1 and y == fc - 1:
    print(d)
else:
    print(-1)