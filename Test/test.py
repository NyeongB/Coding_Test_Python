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

    