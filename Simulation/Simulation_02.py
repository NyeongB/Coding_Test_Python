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

t_num = int(input())

for _ in range(t_num):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

t_num = int(input())

arr_rotate = deque()

for _ in range(t_num):
    t, s = map(str, input().split())
    arr_rotate.append((int(t),s))

time = 0

direction = [(0,1),(1,0),(0,-1),(-1,0)] # 동 남 서 북

snake = deque()  # 
snake.append((0,0,0))
h = {}

while True:
    time += 1

    # 회전 대기 검사
    if len(arr_rotate) !=0 and time == arr_rotate[0][0]:
        r = arr_rotate.popleft()
        print(r[1]+"!!!!!!!!!!")
        ttt = snake[0]
        xx = ttt[0] + direction[ttt[2]][0]
        yy = ttt[1] + direction[ttt[2]][1]
        if r[1] =='L':
            h[(xx,yy)] = (len(snake),3)
            print(h)
        elif r[1] == 'D':
            h[(xx,yy)] = (len(snake),1)


    print(h)

    # 전진
    l = len(snake)
    last = snake.pop()
    snake.append(last)
    for _ in range(l):
        temp = snake.popleft()
        x = temp[0]
        y = temp[1]
        d = temp[2]

        # 회전 확인
        confirm = h.get((x,y),(0,0))
        if str(confirm[1]).isdigit() and confirm[1] != 0:
            if confirm[0] != 0:
                h[(x,y)] = confirm[0] - 1
                x += direction[d][0]
                y += direction[d][1]
                d = (d + confirm[1]) % 4
        else:
            x = x + direction[d][0]
            y += direction[d][1]

        snake.append((x,y,d))

    
    temp = snake[0] # peek

    


    # 충돌검사
    if not (temp[0]>=0 and temp[1] >=0 and temp[0]<n and temp[1] <n) :
        break
    
    l = len(snake)
    flag = 0
    flag2 = 0
    for _ in range(l):
        tt = snake.popleft()
        if flag == 0:
            flag =1
            tt
            snake.append(tt)
            continue
        if temp[0] == tt[0] and temp[1] == tt[1]:
            flag2 = 1
            break
        snake.append(tt)
    if flag2 !=0:
        break

    # 사과 확인
    
    if board[temp[0]][temp[1]] == 1:
        board[temp[0]][temp[1]] = 0
        snake.append(last)
        
        if h.get((temp[0],temp[1])) :
            h[(temp[0],temp[1])] = h.get((temp[0],temp[1]))[0] + 1

    print(snake)

print(time)

'''
'''