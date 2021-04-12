'''
출제 : 백준
난이도 : 골드 4
문제 : 최소 스패닝 트리
날짜 : 21.04.12
유형 : DFS
'''

v, e = map(int, input().split())

graph = list( list([0] * v ) for _ in range(v) )
total = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = graph[b][a] = c

visited = list([0]*v)
visited[0] = 1

def dfs():
    if len(graph) == visited.count(1):
        return

    global total
    min_value = 1000001
    min_index = -1
    for i in range(len(graph)):
        if visited[i] == 1 :
            for j in range(len(graph)):
                if visited[j] == 0:
                    if min_value > graph[i][j]:
                        min_value = graph[i][j]
                        min_index = j

    visited[min_index] = 1
    total += min_value
    dfs()

dfs()
print(total)


'''
'''