'''
출제 : 백준
난이도 : 실버 5
문제 : 좌표정렬하기 2
날짜 : 21.04.10
유형 : 정렬
'''

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x :(x[1],x[0]))

for i in arr:
    print(i[0], i[1])

'''
파이썬 람다 사기
'''