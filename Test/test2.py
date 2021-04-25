import functools

def s(a,b):
    if a < b:
        return -1
    else:
        return 0
    
arr = [1,2,4,3,2,4,2,4]

arr.sort(key= functools.cmp_to_key(s))

print(arr)