'''
출제 : 백준
난이도 : 실버 2
문제 : 효율적인 해킹
날짜 : 21.02.23
유형 : DFS
'''


count = 0
n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visit = [False] * (n+1)
count = [0] * (n+1) # 해킹 최대값들

for _ in range(m):
    x, y = map(int, input().split())
    graph[y][x] = 1


def dfs(v, i):
    visit[v] = True
    for j in range(1,n+1):
        if graph[v][j] == 1 and visit[j] == False:
            count[i] += 1
            dfs(j, i)

for i in range(1,n+1):
    #visit = [False] * (n+1)
    for j in range(n+1):
        visit[j] = False
    dfs(i, i)   # 간선, 인덱스 함께 넘김


result = []
for v, i in enumerate(count):
    if i == max(count):
        result.append(v)

for i in result:
    print(i,end=" ")


'''
메모리 초과
'''