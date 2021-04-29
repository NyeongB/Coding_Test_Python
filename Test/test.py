from itertools import combinations

a = [1,2,3,4,5]

arr = list( list(combinations(a,1)) )

print(arr[0][0])
print(arr[2][0])
print(len(arr[1]))



