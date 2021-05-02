'''
난이도 : 골드 5
문제 : 이중 우선순위 큐
날짜 : 21.05.02
유형 : 힙
'''
import heapq

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    min_heap = []
    max_heap = []
    for _ in range(n):
        command, num = map(str, input().split())
        num = int(num)
        if command =='I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num,num))
        else :
            if len(min_heap) == 0:
                continue
            if num == 1:
                temp = heapq.heappop(max_heap)[1]
                min_heap.remove(temp)
            else:
                temp = heapq.heappop(min_heap)
                max_heap.remove((-temp,temp))

    if len(min_heap) == 0:
        result.append('EMPTY')
    else:
        result.append((heapq.heappop(max_heap)[1], heapq.heappop(min_heap)))

for i in result:
    if i == 'EMPTY':
        print(i)
    else:
        print(i[0], i[1])    

'''
기본 방식으로 했는데 오류남..
아니 시간초과
'''