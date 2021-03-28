'''
출제 : 백준
난이도 : 실버 5
문제 : 회사에 있는 사람
날짜 : 21.03.28
유형 : 해시
'''
n = int(input())
h = dict()
for _ in range(n):
    input_date = input().split()
    k = str(input_date[0])
    d = str(input_date[1])
    if d == 'enter':
        h[k] = 1
    elif d == 'leave':
        h.pop(str(k))
    
a = []    
for i in h.keys():
    a.append(i)

a.sort(reverse=True)

for i in a :
    print(i)


'''
파이썬에는 딕셔너리라는 자료형이 존재
hash()랑 함께 쓰이는것같음
하지만 기본적인 해시 구조로 풀어봄
'''