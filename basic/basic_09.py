'''
출제 : 백준
난이도 : 실버4
문제 : 차집합
날짜 : 21.01.21
유형 : 자료구조
'''
n1,n2 = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

aSet = set(a)
bSet = set(b)

result = list(aSet-bSet)
result.sort()

print(len(result))
for i in result:
    print(i,end=' ')