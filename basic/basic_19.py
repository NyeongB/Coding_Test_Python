'''
출제 : 백준
난이도 : 실버 4
문제 : 소수 찾기
날짜 : 21.04.11
유형 : 수학
'''

def isPrime(n):
    if n <=1:
        return False
    
    for i in range(2, int(n**0.5) + 1 ):
        if n % i == 0:
            return False
    
    return True

n = int(input())
count = 0
arr = list(map(int, input().split()))

for i in arr:
    if isPrime(i):
        count += 1
print(count)
'''
조합 nCr 을 itertools로 라이브러리를 통해 구현해봤다.
'''

