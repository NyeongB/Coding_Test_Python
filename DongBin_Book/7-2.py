# 21.01.22
# p.205
# 떡볶이 떡 만들기

n, target = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
start = 0
end = max(arr)  # 0 ~ 가장 긴 떡길이까지 
mid = 0
while start<=end:
    mid = (start+end) // 2
    result = 0

    for i in arr:
        if i - mid > 0:
            result += i - mid
    
    if result > target:
        start = mid + 1
    else:
        end = mid - 1

print(mid)

    