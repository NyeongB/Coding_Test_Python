'''
출제 : 백준
난이도 : 실버 3
문제 : 수열
날짜 : 21.04.30
유형 : 수열
'''


n, k = map(int, input().split())

arr = list(map(int, input().split()))
Max = -1e9

total = sum(arr[:k])
Max = total
i = 0
if k == 1:
    print(max(arr))
else:
    while True:
        total -= arr[i]
        if i + k >= n:
            break 
        total += arr[i+k]
        Max = max(total, Max)
        i += 1
    print(Max)



'''
n, k = map(int, input().split())

arr = list(map(int, input().split()))
Max = -1e9
for i in range(n):
    Max = max(sum(arr[i:i+k]),Max)

print(Max)
'''
# 처음 쓴 코드 시간 초과..
# 좋은 걸 배워가는 문제
# 연속된 수의 합은 앞으로 이런식으로 풀어야겠다.