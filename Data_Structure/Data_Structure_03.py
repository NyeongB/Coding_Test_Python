'''
출제 : 백준
난이도 : 실버 1
문제 : 최소 힙
날짜 : 21.04.13
유형 : 최소 힙
'''

import sys
import heapq

n = int(sys.stdin.readline().rstrip())
result = []

min_heap  = []
#heapq.heapify(min_heap) 기존에 리스트를 힙으로 만들기 굳이 안해줘도 됨 

for _ in range(n):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        if len(min_heap) == 0:
            result.append(0)
        else :
            result.append(heapq.heappop(min_heap))
    else :
        heapq.heappush(min_heap, temp)

for i in result:
    print(i)
