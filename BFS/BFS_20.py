'''
출제 : 백준
난이도 : 실버 2
문제 : 나이트의 이동
날짜 : 21.06.07
유형 : BFS
'''
from collections import deque
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,-1,1,-2,-2]

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    visited = [[False]*n for _ in range(n)]
    start = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))
    q = deque()
    q.append( (start[0],start[1],0) )
    visited[start[0]][start[1]] = True
    while q:
        temp = q.popleft()
        if (temp[0],temp[1]) == (end[0], end[1]):
            result.append(temp[2])
            break
        for idx in range(8):
            nx = temp[0] + dx[idx]
            ny = temp[1] + dy[idx]

            if 0<= nx <n and 0<= ny <n:
                if not visited[nx][ny]:
                    q.append((nx,ny,temp[2]+1))
                    visited[nx][ny] = True


for i in result:
    print(i)

'''
bfs 문제
'''