'''
출제 : 백준
난이도 : 골드 4
문제 : 아기 상어
날짜 : 21.04.19
유형 : BFS
'''
from collections import deque
import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = (i, j)


dir = [(1,0),(-1,0),(0,1),(0,-1)]


def find_min(t, x, y, size):
    
    graph[x][y] = 0
    queue = deque()
    queue.append((t,x,y))
    m = len(graph)
    heap = []
    visited = set()
    while queue:
        t, t_x, t_y = queue.popleft()
        visited.add((t_x,t_y))
        for i in dir:
            nx = t_x + i[0]
            ny = t_y + i[1]
            if 0<= nx < m and 0 <= ny < m and (nx,ny) not in visited:
                visited.add((nx,ny))

                if graph[nx][ny] == 0 or graph[nx][ny] == size:
                    queue.append((t+1, nx, ny))
                    continue

                if graph[nx][ny] > size:
                    continue
                else:
                    heapq.heappush(heap,(t+1, nx, ny))
    

    if heap:
        return heap[0]
    else :
        return None


time = 0
size = 2
eat = 0
while True:

    next = find_min(0, sx, sy, size)
    
    
    if next is None:
        break

    t, sx, sy = next
    time += t

    eat += 1

    if eat == size:
        size += 1
        eat = 0

print(time)

'''
heap 과 bfs 쓰는 문제
레퍼런스를 보고 이해하는데도 굉장히 오래걸렸다
바로 다시 풀어본다.
'''