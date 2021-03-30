'''
난이도 : 실버 3
문제 : 풍선 터뜨리기
날짜 : 21.03.30
유형 : 덱
'''
from collections import deque

n = int(input())

a = list(map(int, input().split()))

b = deque()

for i, v in enumerate(a):
    b.append((i+1,v))

result = []


result.append(b[0][0])
d = b.popleft()[1]

while b:
    if d>0:
        for _ in range(d-1):
            b.append(b.popleft())
        d = b[0][1]
        result.append(b.popleft()[0])
    else :
        d = d * -1
        for _ in range(d-1):
            b.appendleft(b.pop())
        d = b[-1][1]
        result.append(b.pop()[0])

for i in result:
    print(i,end=' ')


'''
덱의 기본문제인듯 
요세푸스 문제 진화형?
'''