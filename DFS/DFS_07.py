'''
출제 : 백준
난이도 : 실버 2
문제 : 유기농 배추
날짜 : 21.03.25
유형 : DFS
'''
import sys

sys.setrecursionlimit(10000)

d = [(0,-1),(0,1),(1,0),(-1,0)]
n = int(input())
a = []
result = []
count = 0

def dfs(x, y,n,m):
    a[x][y] = 0
    for i in d:
        dx = x + i[0]
        dy = y + i[1]
        if 0<= dx < n and 0<= dy < m:
            if a[dx][dy] == 1:
                a[dx][dy] = 0
                dfs(dx,dy,n,m)

for _ in range(n):
    count = 0
    y, x, t = map(int, input().split())
    a = [ ( [0] * y ) for _ in range(x) ]
    for _ in range(t):
        m,n = map(int, input().split())
        a[n][m] = 1
    for i in range(x):
        for j in range(y):
            if a[i][j] == 1 :
                count = count + 1
                dfs(i,j,x,y)
    result.append(count)

for i in result:
    print(i)

    
'''
런타임 에러가 계속떠서 찾아보니 

import sys

sys.setrecursionlimit(10000)

이걸 추가하면 바로 해결됐다

원인을 찾아보자.. 

'''
