'''
출제 : 백준
난이도 : 실버 1
문제 : 데스 나이트
날짜 : 21.01.19
유형 : BFS
'''
from collections import deque


n = int(input())

r1,c1,r2,c2 = map(int,input().split())
graph = [([0] * n) for _ in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x, y):

    queue = deque()
    queue.append([x,y,0])
    graph[x][y] = 1
    if x == r2 and y == c2:
        return 0

    while queue : 
        temp = queue.popleft()
        for i in range(6):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx == r2 and ny == c2 :
                return temp[2] + 1
            if 0<=nx<n and 0<=ny<n :
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append([nx,ny,temp[2]+1])

    return -1

print(bfs(r1,c1))

'''
처음에 i를 4까지 돌려서 테스트케이스3이 계속 오류나길래 뭔가했다..
4방향을 맨날 하다보니 습관성으로 외워버린거같은데
바로 코드를 풀기보단 어떻게 접근할건지 계획세우고 해야겠다..
'''