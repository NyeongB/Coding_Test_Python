'''
출제 : 백준
난이도 : 실버 5
문제 : 쉽게푸는문제
날짜 : 21.04.05
유형 : 구현
'''
a, b = map(int, input().split())

arr = []

for i in range(1, b+1):
    for _ in range(i):
        arr.append(i)

print(sum(arr[a-1:b]))

'''
파이썬의 사기적인 sum(배열[시작:끝인덱스])를 경험해보았고
문제가 처음에 시간초과 날거같은데 그냥 풀었다.
'''