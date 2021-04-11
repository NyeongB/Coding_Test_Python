'''
출제 : 백준
난이도 : 실버 4
문제 : 두 수의 합
날짜 : 21.04.11
유형 : 정렬
'''

'''
9
5 12 7 10 9 1 2 3 11
13
'''

n = int(input())

arr = list(map(int,input().split()))
target = int(input())
arr.sort()
count = 0
while True:

    if len(arr) == 1:
        if arr[0] == target:
            count += 1
        arr.pop()

    if arr == []:
        break

    temp = arr[0] + arr[-1]
    if temp == target:
        count += 1
        arr.pop(0)
        arr.pop()
    elif temp < target:
        arr.pop(0)
    elif temp > target:
        arr.pop()

print(count)

'''

'''