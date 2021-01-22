# 21.01.22
# p.198
# 부품 찾기

import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(input())
x = list(map(int,sys.stdin.readline().rstrip().split()))

def binary_search(array, start, end, target):

    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
    
    return None

arr.sort()

for i in x:
    result = binary_search(arr, 0, n-1, i)

    if result != None:
        print("yes",end=" ")
    else:
        print("no", end=" ")

