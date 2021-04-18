'''
출제 : 백준
난이도 : 브론즈 2 
문제 : 시험 감독
날짜 : 21.04.18
유형 : 구현
'''
import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

mans = 0

for i in a:
    if i <= b:
        mans += 1
        continue
    else:
        i -=b
        mans +=1
        mans += math.ceil(i/c)

print(mans)