'''
문제 : 상하좌우
날짜 : 21.03.22
유형 : 구현
'''

n = int(input())

command = list(map(str, input().split()))
nx = 1
ny = 1
dx = [-1,0,1,0] # 상 우 하 좌
dy = [0,1,0,-1]

for i in command:
    if i =='U':
        if 1<=nx + dx[0]<=n and 1<= ny + dy[0] <=n:
            nx = nx + dx[0]
            ny = ny + dy[0]
    elif i =='R':
        if 1<=nx + dx[1]<=n and 1<= ny + dy[1] <=n:
            nx = nx + dx[1]
            ny = ny + dy[1]
    elif i =='D':
        if 1<=nx + dx[2]<=n and 1<= ny + dy[2] <=n:
            nx = nx + dx[2]
            ny = ny + dy[2]
    elif i =='L':
        if 1<=nx + dx[3]<=n and 1<= ny + dy[3] <=n:
            nx = nx + dx[3]
            ny = ny + dy[3]        

print(nx,ny)    
'''
책은 정말 깔끔하게 풀었다
x, dx, nx 를 나누고 
0~3 인덱스에 맞는 방향 타입도 정하고 문제를 해결하였다.
'''