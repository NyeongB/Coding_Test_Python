import heapq

a = [5,4,3,2,1,]

heapq.heapify(a)
heapq.heappush(a,0)
print(heapq.heappop(a))
print(a)