'''
출제 : 백준
난이도 : 실버 5
문제 : 나이순 정렬
날짜 : 21.01.24
유형 : 정렬
'''

n = int(input())

arr = []

for _ in range(n):
    input_data = input().split()
    arr.append( (int(input_data[0]), input_data[1]) )

arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0],i[1])

'''
정수와 문자열을 따로 받고 
labmda x:x[0] 으로 정수 기준으로 오름차순정렬
'''