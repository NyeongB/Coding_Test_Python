'''
출제 : 백준
난이도 : 실버 2
문제 : 최대 힙
날짜 : 21.04.13
유형 : 최대 힙
'''
import heapq

heap = []

n = int(input())

result = []

for _ in range(n):
    temp = int(input())

    if temp == 0 :
        if len(heap) == 0:
            result.append(0)
        else :
            result.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-temp,temp))

for i in result:
    print(i)

'''
최소 힙 응용 외우도록 하자
'''