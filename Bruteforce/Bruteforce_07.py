'''
출제 : 백준 
난이도 : 실버 5
문제 : 영화감독 숌
날짜 : 21.05.30
유형 : 브루트포스
'''
n = int(input())
sum = 0
while n > 0:
    sum += 1
    s = str(sum)
    if '666' in s:
        n -= 1

print(sum)

'''
굉장히 중요한 문제
생각의 전환이 되는 문제이다 
'''