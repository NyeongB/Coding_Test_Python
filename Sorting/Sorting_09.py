'''
출제 : 백준
난이도 : 실버 5
문제 : 좌표 정려
날짜 : 21.04.25
유형 : 정렬
'''
n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort(key=lambda x : (x[0],x[1]))

for i in arr:
    print(i[0],i[1])