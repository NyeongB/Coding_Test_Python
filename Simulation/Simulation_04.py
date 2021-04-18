'''
출제 : 백준
난이도 : 실버 1
문제 : 톱니바퀴(2)
날짜 : 21.04.18
유형 : 시뮬레이션
'''

import sys
from collections import deque
n = int(input())

arr = deque()

for _ in range(n):
    arr.append(deque(map(int, sys.stdin.readline().rstrip())))

k = int(input())

temp = []
for _ in range(k):
    temp.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

visited = [0]*n
#print(visited)
def rotate(index, d):
    #print(index,d)
    if visited[index] == 1:
        #print(str(index)+"out")
        return
    else:
        visited[index] = 1
    # 첫번째
    if index == 0:
        if arr[0][2] != arr[1][6]:
            
            rotate(1, -1 * d)
    # 마지막 
    elif index == len(arr)-1:
        if arr[index][6] != arr[index-1][2]:
            
            rotate(index-1,-1*d)
    # 가운데
    else:
        if arr[index][6] != arr[index-1][2]:
            
            rotate(index-1, -1*d)
        
        if arr[index][2] != arr[index+1][6]:
            
            
            rotate(index+1,-1*d)

    if d == 1:
        arr[index].appendleft(arr[index].pop())
    elif d == -1:
        arr[index].append(arr[index].popleft())
    



for i in temp:
    a, b = i
    rotate(a-1,b)
    visited = [0]*n
    
answer = 0

for i in arr:
    if i[0] == 1:
        answer += 1

print(answer)
    
'''
돌리는거는 덱으로 판단했고
가능할때 rotate를 돌렸다
문제는 방문기록을 하지않아서 계속 rotate가 돌리며 무한 루프에 빠진걸 뒤늦게 판단하고
방문기록을 추가했다..
'''    