'''
출제 : 백준
난이도 : 실버1
문제 : 골드바흐의 추측
날짜 : 21.03.22
유형 : 
'''
import math

s = "Goldbach's conjecture is wrong."


def prime(n):
    t = int(math.sqrt(n))
    for i in range(2, t+1):
        if n % i == 0:
            return False

    return True


a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

for i in a:
    t1 = i
    flag = 1
    for j in range(3, i, 2):
        if prime(j):
            if prime(t1 - j):
                print(str(t1)+ " = " + str(j) + " + "+ str(t1-j))
                flag = 0
                break
    if flag == 1:
        print(s)

'''
pypy 532ms
python3 3122ms
3초 넘어갔는데 맞았다고 하는데 이거 체크
'''