'''
출제 : 백준
난이도 : 실버 3
문제 : 연결 요소의 개수
날짜 : 21.02.23
유형 : DFS
'''


count = 0
n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1


def dfs(x) :
    visit[x] = True
    for i in range(1,n+1):
        if graph[x][i] == 1 and visit[i] == False :
            dfs(i)


for i in range(1,n+1):
    if visit[i]==False:
        dfs(i)
        count += 1

print(count)

'''
파이썬 문법 공부 제대로 해야겠다고 느꼈다..
반복문의 범위를 헷갈려하다니
'''