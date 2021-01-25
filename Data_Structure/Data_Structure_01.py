'''
출제 : 백준
난이도 : 실버 5
문제 : 요세푸스 문제
날짜 : 21.01.25
유형 : 큐
'''
from collections import deque
n, k = map(int,input().split())

input_data = [i for i in range(1,n+1)]
q = deque(input_data)
result = []
while q :
    for _ in range(k-1):
        temp = q.popleft()
        q.append(temp)
    result.append(q.popleft())

print("<"+str(result.pop(0)),end="")

for i in result:
    print(", "+str(i),end="")
print(">",end="")
