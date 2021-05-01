'''
출제 : 백준
난이도 : 실버 3
문제 : 이전 수열
날짜 : 21.05.01
유형 : 수열
'''


from itertools import permutations

n = int(input())
a = tuple(map(int, input().split()))
nums = [i for i in range(1,n+1)]

arr = list(permutations(nums,n))

for i,v in enumerate(arr):
    if v == a:
        idx = i
        break


if idx ==0:
    print(-1)
else:
    print(' '.join(map(str,arr[idx-1])))

    
'''
메모리 초과..? 
단순하게 순열로 생각했지만 
알고리즘적인 접근이 필요한것같다
이 부분이 항상 부족함..!
'''