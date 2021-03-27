'''
난이도 : 실버 5
문제 : 요세푸스 문제
날짜 : 21.03.27
유형 : 큐
'''
from collections import deque

n, k = map(int, input().split())

input_data = [i for i in range(1, n+1)]

q = deque(input_data)
r = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    r.append(q.popleft())

print("<", end='')
for i in range(0, len(r)-1):
    print(r[i], end=", ")
print(str(r[-1]) + ">",end='')  



'''
처음에 기본 리스트안에서 pop(0)를 사용하여 문제를 접근했는데
시간초과가 났다
앞으로 큐 관련된것은 무조건 from collections import deque / q = deque() / q.popleft() 로 접근한다!
'''