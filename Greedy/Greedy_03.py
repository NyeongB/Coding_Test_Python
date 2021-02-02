'''
출제 : 백준
난이도 : 브론즈 1
문제 : 설탕배달
날짜 : 21.02.02
유형 : 그리디
'''
import sys

n = int(input())

# 가장 큰 수부터 나누어 본다.

if n % 5 == 0 :
    print(n//5)
    sys.exit()
else:
    k = n//5
    temp = n
    for i in range(k,0,-1):
        temp = n
        temp -= 5*i
        if temp % 3==0:
            print(i+temp//3)
            sys.exit()

if n % 3 ==0:
    print(n//3)
else : 
    print(-1)

'''
브론즈1은 아닌거같은 문제..
'''