from itertools import permutations
import sys

n = int(input())

nums = list(map(int,input().split()))

d = list(map(int,input().split()))
arr = []

for i,v in enumerate(d):
    for _ in range(v):
        arr.append(i)
#print(arr)
op = list(set(list(permutations(arr,len(nums)-1))))
#print(op)
Max = -sys.maxsize - 1
Min = sys.maxsize
#print(nums)
for i in op:
    total = nums[0]
    for index, j in enumerate(i):
        if j == 0:
            total += nums[index+1]
        elif j == 1:
            total -= nums[index+1]
        elif j == 2:
            total *= nums[index+1]
        elif j == 3:
            total = int(total / nums[index+1])
    Min = min(total,Min)
    Max = max(total,Max)

print(Max)
print(Min)