'''
출제 : 백준
난이도 : 실버 1
문제 : 토마토
날짜 : 21.01.18
유형 : BFS
'''
from collections import deque
import sys

m, n = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0   # 마지막에 찍히는 카운터가 걸린 날짜

def bfs() : 
    queue = deque()

    # 처음에 다 넣어야 함, 여러군대에서 토마토 시작
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i,j,0])


    while queue :
        temp = queue.popleft()
        global count
        count = temp[2]
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 1
                    queue.append([nx,ny,count+1])   # 큐에 넣을때 날짜 +1
            


bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print("-1")
            sys.exit()


print(count)