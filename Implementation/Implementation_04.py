'''
출제 : 백준
난이도 : 실버 2
문제 : 배열 돌리기 3
날짜 : 21.04.18
유형 : 구현
'''

import sys

n, m, r = map(int, sys.stdin.readline().rstrip().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    
op = list(map(int, sys.stdin.readline().rstrip().split()))



def one(arr):
    n = len(arr)
    m = len(arr[0])
    
    temp = list(([0]*m) for _ in range(n))

    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[n-1-i][j]
    return temp

def two(arr):
    n = len(arr)
    m = len(arr[0])
    
    temp = list(([0]*m) for _ in range(n))

    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][m-1-j]
    return temp

def three(arr):
    n = len(arr)
    m = len(arr[0])

    n,m = m,n

    temp = list(([0]*m) for _ in range(n))

    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[m-1-j][i]
    return temp

def four(arr):
    n = len(arr)
    m = len(arr[0])

    n,m = m,n

    temp = list(([0]*m) for _ in range(n))

    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[j][n-1-i]
    return temp

def five(arr):
    n = len(arr)
    m = len(arr[0])
    temp = list(([0]*m) for _ in range(n))
    N = n//2
    M = m//2

    for i in range(N):
        for j in range(M):
            temp[i][j+M] = arr[i][j]

    for i in range(N):
        for j in range(M):
            temp[i+N][j+M] = arr[i][j+M]

    for i in range(N):
        for j in range(M):
            temp[i+N][j] = arr[i+N][j+M]

    for i in range(N):
        for j in range(M):
            temp[i][j] = arr[i+N][j]


    return temp

def six(arr):
    n = len(arr)
    m = len(arr[0])
    temp = list(([0]*m) for _ in range(n))
    N = n//2
    M = m//2

    for i in range(N):
        for j in range(M):
            temp[i+N][j] = arr[i][j]

    for i in range(N):
        for j in range(M):
            temp[i+N][j+M] = arr[i+N][j]

    for i in range(N):
        for j in range(M):
            temp[i][j+M] = arr[i+N][j+M]

    for i in range(N):
        for j in range(M):
            temp[i][j] = arr[i][j+M]


    return temp 


for i in op:
    if i == 1:
        arr = one(arr)
    elif i == 2:
        arr = two(arr)
    elif i == 3:
        arr = three(arr)
    elif i == 4:
        arr = four(arr)
    elif i == 5:
        arr = five(arr)
    elif i == 6:
        arr = six(arr)
    

for i in arr:
    print(' '.join(map(str,i)),end='\n')