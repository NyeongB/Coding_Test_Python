'''
출제 : 백준
난이도 : 실버 2
문제 : 연결 요소의 갯수
날짜 : 21.05.29
유형 : DFS
'''
n, m = map(int, input().split())

graph = list([0]*(n+1) for _ in range(n+1) )
visited = [True] * (n+1)
count = 0

def dfs(i):
    visited[i] = False
    for j in range(1,n+1):
        if graph[i][j] == 1 and visited[j]:
            dfs(j)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

for i in range(1, n+1):
    if visited[i]:
        dfs(i)
        count += 1

print(count)