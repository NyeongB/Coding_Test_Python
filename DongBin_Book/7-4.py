'''
문제 : 떡볶이 떡 만들기
날짜 : 21.04.25
유형 : binary search
'''

n, target = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

start = 0
end = max(arr)
result = 0
while start <= end:
    mid = (start+end)//2

    total = 0
    for i in arr:
        if i - mid <=0:
            continue
        else:
            total += i - mid
    
    
    if total < target:
        end = mid - 1
    else:
        start = mid+1
        result = mid


print(result)


'''
4 6
19 15 10 17
->
15
'''