'''
출제 : 백준
난이도 : 실버 5
문제 : 좌표 정렬하기
날짜 : 21.01.20
유형 : 정렬
'''

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int,input().split())))
array.sort()

for i, j in array:
    print(i,j)

'''
584ms	PyPy3 
4244ms  python3
'''