'''
출제 : 백준
난이도 : 골드 5
문제 : 마법사 상어와 파이어볼
날짜 : 21.04.24
유형 : 구현
'''
from collections import deque
import math
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

n, m1, k = map(int, input().split())

arr = [ [deque() for _ in range(n)] for _ in range(n)]

for _ in range(m1):
    r, c, m, s, d = map(int,input().split())
    arr[r-1][c-1].append((m,s,d))

for _ in range(k):

    # 이동
    temp = [([0]*n)for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = len(arr[i][j])

    for i in range(n):
        for j in range(n):

            for t in range(temp[i][j]):
                x,y = i,j
                m,s,d = arr[i][j].popleft()
                for _ in range(s):
                    x = (x + dx[d]) % n
                    y = (y + dy[d]) % n
                arr[x][y].append((m,s,d))


    # 합체 분산
    temp = [([0]*n)for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = len(arr[i][j])        

    
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 1:
                nm, ns, odd, even, flag = 0, 0, 0, 0, 0
                for idx, [m, s, d] in enumerate(arr[i][j]):
                    nm += m
                    ns += s
                    if idx == 0:
                        if d % 2 == 0:
                            even = 1
                        else:
                            odd = 1
                    else:
                        if even == 1 and d % 2 == 1:
                            flag = 1
                        elif odd == 1 and d % 2 == 0:
                            flag = 1

                nm //= 5
                ns //= len(arr[i][j])
                arr[i][j] = deque()
                if nm != 0:
                    for idx in range(4):
                        nd = 2 * idx if flag == 0 else 2 * idx + 1
                        arr[i][j].append([nm, ns, nd])

#print(arr)
ans = 0
for i in range(n):
    for j in range(n):     
        l = len(arr[i][j])
        if l ==0:
            continue
        
        for _ in range(l):
            m,s,d = arr[i][j].popleft()
            ans += m

print(ans)


