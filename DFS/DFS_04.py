'''
출제 : 백준
난이도 : 실버 1
문제 : 섬 연결하기
날짜 : 21.01.31
유형 : DFS
'''

dx = [0,0,-1,1]
dy = [1,-1,0,0]
graph = []
count = 0
answer = []
n = int(input())
c = 0
def dfs(x, y):
    graph[x][y] = 2
    global c
    c += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny <0 or nx>=n or ny >= n:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)
    return c

for _ in range(n):
    graph.append(list(map(int,input())))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            c = 0
            answer.append(dfs(i,j))
            count += 1

print(count)
answer.sort()
for i in answer:
    print(i)

'''
c 를 글로벌로해서 dfs가 돌때마다 갯수를 함께 세었다
'''