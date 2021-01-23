'''
출제 : 백준
난이도 : 실버4
문제 : 터렛
날짜 : 21.01.23
유형 : 기하학
'''
import math

n = int(input())

answer = []

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    i = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    
    if x1 == x2 and y1 == y2 :
        if r1 == r2:
            answer.append(-1)
        else :
            answer.append(0)
    elif i == (r1+r2) or i == abs(r1-r2):  
        answer.append(1)
    elif (r1+r2) > i > abs(r1-r2):
        answer.append(2)
    else:
        answer.append(0)

for i in answer:
    print(i)

'''
두 원이 겹치는 정도를 봐야함 
무한대라고 하면 같은 좌표 같은 반지름을 같는 두원 -1 
반지름이 다르면 0 

그리고 서로 다른 좌표를 가지면 두점사이의 거리와 반지름의 길이로 0 1 2 를 판단할 수 있다.
'''