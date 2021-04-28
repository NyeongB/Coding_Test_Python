'''
출제 : 백준
난이도 : 실버 1
문제 : 숨바꼭질
날짜 : 21.04.28
유형 : BFS
'''
from collections import deque

start, end = map(int, input().split())

queue = deque()

visited = set()
visited.add(start)
result = 0

queue.append((start, 0))    # 시작 위치와 초

while queue:
    x, t = queue.popleft()
    if x == end:
        result = t

    if x + 1 <= 100000 and x + 1 not in visited:
        queue.append((x+1, t+1))
        visited.add(x+1)
    
    if 0 <= x - 1 and x - 1 not in visited:
        queue.append((x-1, t+1))
        visited.add(x-1)
    
    if x * 2 <= 100000 and x * 2 not in visited:
        queue.append((x*2, t+1))
        visited.add(x*2)

print(result)