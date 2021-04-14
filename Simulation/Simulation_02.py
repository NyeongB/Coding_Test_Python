'''
출제 : 백준
난이도 : 골드 5
문제 : 뱀
날짜 : 21.04.14
유형 : 시뮬레이션
'''
from collections import deque

n = int(input())

board = list(list([0]*n) for _ in range(n))

k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
h = {}
for _ in range(l):
    t, s = map(str, input().split())
    h[int(t)] = s

visited = deque()
visited.append((0,0))   # 방문기록
board[0][0] = 2
x = 0
y = 0
d = [(0,1),(1,0),(0,-1),(-1,0)] # 동 남 서 북
index = 0   # 방향 인덱스
time = 1

while True:
    # 이동
    x = x + d[index][0]
    y = y + d[index][1]

    if 0<= x <n and 0<= y <n and board[x][y] !=2:
        # 구현
        if not board[x][y] == 1:  # 사과가 없는 경우
                temp_x, temp_y = visited.popleft()
                board[temp_x][temp_y] = 0  # 꼬리 제거
        board[x][y] = 2
        visited.append([x, y])
        if time in h.keys():
            if h[time] =='L':
                index = (index+3)%4
            elif h[time] =='D':
                index = (index+1)%4
        time +=1
    else:
        break

print(time)

'''
3시간 걸렸다.. 
결국 레퍼런스를 참고하긴했지만 많은것을 배웠다.
처음 코드는 정말 뱀이 돌고 도는걸 구현해볼려했는데
레퍼런스를 보면 방문기록으로 다 해결이 가능하다.
'''