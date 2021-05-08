'''
출제 : 백준
난이도 : 실버 4
문제 : 문자열
날짜 : 21.05.08
유형 : 문자열
'''

str_a, str_b = map(str,input().split())
ans = 1e9
n = len(str_b) - len(str_a)

for i in range(n+1):
    count = 0
    for j in range(len(str_a)):
        if str_a[j] != str_b[j+i]:
            count += 1
    if ans > count:
        ans = count

print(ans)

'''
정말 중요한 문제같다.. 
아직도 내 머리는 알고리즘다운 접근을 하지않는듯.. 
추가적으로 생기는 문자열은 당연히 다 같다고 생각하고 이문제를 접근해야지
모든 부분의 알파벳을 접근하려했다..
'''