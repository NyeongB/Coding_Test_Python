'''
출제 : 백준
난이도 : 실버 3
문제 : 바이러스
날짜 : 21.03.31
유형 : DFS
'''

n = int(input())
m = int(input())

graph = list( list([0] * n) for _ in range(n)  )
visited = list([False] * n)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = graph[y-1][x-1] = 1

count = 0

def dfs(v):
    visited[v] = True
    global count
    for i in range(n):
        if not visited[i] and graph[v][i] == 1:
            count += 1
            visited[i] = True
            dfs(i)
dfs(0)
print(count)

'''
방향이 없고 연결만 되있다는걸로 dfs하는 인접행렬 문제
재귀로 곧바로 구현해보았다.
'''