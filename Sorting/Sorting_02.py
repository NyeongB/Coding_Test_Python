'''
출제 : 백준
난이도 : 실버 5
문제 : K번쨰 수
날짜 : 21.01.20
유형 : 정렬
'''

n, m = map(int,input().split())

array = list(map(int,input().split()))

array.sort()

print(array[m-1])

'''
pypy3 2854ms가 나왔는데 제대로된 정답인가 싶다
자바에선 안됐을거다
'''