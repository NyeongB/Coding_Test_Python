'''
출제 : 백준
난이도 : 실버 5
문제 : 단어 정렬
날짜 : 21.03.27
유형 : 정렬
'''

n = int(input())
arr = []
for _ in range(n):
    input_data = input()
    a = len(input_data)
    arr.append( (a, input_data) )

arr = list(set(arr))

arr.sort(key= lambda x: (x[0],x[1]) )

for i in arr:
    print(i[1])