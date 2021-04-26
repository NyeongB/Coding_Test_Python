'''
출제 : 백준
난이도 : 실버 3
문제 : 나무 자르기
날짜 : 21.04.26
유형 : 이분 탐색
'''

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start+end)//2

    total = 0
    for x in arr:
        if x - mid > 0:
            total += x - mid
    
    if m > total:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
