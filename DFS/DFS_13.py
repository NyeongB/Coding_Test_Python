'''
출제 : 백준
난이도 : 실버 1
문제 : 단지번호붙이기
날짜 : 21.05.21
유형 : DFS
'''

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(i,j,count,n):
    arr[i][j] = count
    for idx in range(4):
        nx = dx[idx] + i
        ny = dy[idx] + j
        if 0<= nx <n and 0 <= ny <n:
            if arr[nx][ny] == 1:
                dfs(nx,ny,count,n)

n = int(input())
count = 1
arr = [list(map(int,input()))for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            count += 1
            dfs(i,j,count,n)


for k in range(1,count):
    c = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]-1 == k:
                c += 1
    result.append(c)
result.sort()
print(count-1)
for i in result:
    print(i)