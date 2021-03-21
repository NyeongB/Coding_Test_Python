'''
출제 : 백준
난이도 : 실버 4
문제 : 보물
날짜 : 21.03.21
유형 : 정렬
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
b.reverse()

sum = 0

for i in range(n):
    sum += a[i] * b[i]

print(sum)

'''
reverse는 이미 오름차순 된거 기준으로
'''