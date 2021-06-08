'''
출제 : 백준
난이도 : 실버 3
문제 : 대칭 차집합
날짜 : 21.06.08
유형 : 집합
'''
n, m = map(int,input().split())

a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(a-b)+len(b-a))

'''
이걸 원한게 아는거같은데 쉽게 풀린다..
'''