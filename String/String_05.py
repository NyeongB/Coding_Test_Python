'''
출제 : 백준
난이도 : 실버 2
문제 : 투에-모스 문자열
날짜 : 21.04.12
유형 : 문자열
'''
n = int(input())


def rev(s):
    s2 = ''
    for i in s:
        if i =='0':
            s2 += '1'
        else :
            s2 += '0'
    
    return s2

def convert(n):
    n2 = 0
    while True:
        if n >= 2**n2:
            n2 += 1
        else:
            break
    return n2


dp = []
dp.append('0')

for i in range(1,convert(n)+1):
    dp.append(dp[i-1]+rev(dp[i-1]))

print(dp.pop()[n-1])


'''
시간초과....... 다시 꼭 풀어본다
이거 참고할 레퍼런스도 없어서 다시 꼭 해봐야지
분명히 비트 연산자로 해야한다.
시간초과 계속 나네..
'''