'''
출제 : 백준
난이도 : 실버 1
문제 : 미로 탐색
날짜 : 21.04.22
유형 : BFS
'''
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int, input().split())

arr = [list(map(int, input())) for _ in range(n)]

visited = set()

q = deque()

q.append((0,0,1))
visited.add((0,0))

while q:
    x, y, r = q.popleft()
    if x == n-1 and y == m-1:
        print(r)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if (nx, ny) not in visited and arr[nx][ny] == 1:
                q.append((nx,ny,r+1))
                visited.add((nx,ny))