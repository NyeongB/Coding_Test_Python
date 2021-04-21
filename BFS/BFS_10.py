'''
출제 : 백준
난이도 : 골드 5
문제 : 인구 이동
날짜 : 21.04.21
유형 : BFS
'''
'''
출제 : 백준
난이도 : 골드 5
문제 : 인구 이동
날짜 : 21.04.21
유형 : BFS
'''
from collections import deque

n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dir = [(0,1),(0,-1),(-1,0),(1,0)]
def bfs(x, y, visited):
    global n, l, r
    result = []
    result.append((x,y))
    visited.add((x,y))
    q = deque()
    q.append((x,y))

    
    while q:
        nx, ny = q.popleft()
        for i in dir:
            dx = nx + i[0]
            dy = ny + i[1]

            if 0<= dx < n and 0<= dy < n and (dx,dy) not in visited:
                if l <= int(abs(arr[nx][ny] - arr[dx][dy])) <= r:
                    result.append((dx,dy))
                    visited.add((dx,dy))
                    q.append((dx,dy))

    if len(result) == 1:
        return 0

    size = 0
    sum = 0
    #print(result)
    for i in result:
        sum += arr[i[0]][i[1]]
        size +=1
    
    for i in result:
        arr[i[0]][i[1]] = sum // size
        
    return 1


t = 0

while True:
    visited = set()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if (i,j) not in visited:
                cnt += bfs(i, j, visited)
    
    if cnt == 0:
        break
    t += 1

print(t)

