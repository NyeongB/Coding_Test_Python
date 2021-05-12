from itertools import combinations

arr = [1,2,3,4,5]

a = list(combinations(arr,3))

for i in a:
    print(', '.join(map(str,i)),end='\n')