'''
출제 : 백준
난이도 : 실버 2
문제 : 차이를 최대로
날짜 : 21.04.11
유형 : 순열
'''

from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))

a = list(permutations(arr, len(arr)))

result = 0
for i in a:
    sum = 0
    for j in range(n-1):
        sum += abs(i[j] - i[j+1])
    
    result = max(sum, result)

print(result)


'''
이건 뭐 모든 경우의 수를 다 봐야함

p(arr) == p(arr,len(arr))
permutations 하나만 쓰면 모든 경우 다 보는거로 침 
'''

