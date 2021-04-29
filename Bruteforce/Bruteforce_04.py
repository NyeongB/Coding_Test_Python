'''
출제 : 백준
난이도 : 골드 5
문제 : 보물섬
날짜 : 21.04.29
유형 : 브루트포스 / BFS
'''

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

n, m = map(int, input().split())

graph = [list(map(str,input())) for _ in range(n)]

start_points = deque()
#print(graph)
Max = -1e9

# 시작 지점 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            start_points.append((i,j))


def bfs(x, y):
    q = deque()
    q.append((x,y,0))
    visited = set()
    visited.add((x,y))
    ans = 0
    while q:
        x, y, d = q.popleft()
        ans = d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if graph[nx][ny] == 'L':
                    visited.add((nx,ny))
                    q.append((nx,ny,d+1))

    return ans

while start_points:
    x, y = start_points.popleft()

    Max = max(bfs(x, y), Max)
    #print(x,y,Max)
print(Max)

'''
처음 BFS를 돌때 초기로 방문한 x,y에 값을 방문처리를 안해서 오류가 났다.
bfs할때 항상 자기 자신을 방문처리하는 습관을 기른다.

'''

