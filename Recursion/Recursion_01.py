'''
출제 : 백준
난이도 : 실버3
문제 : 1,2,3 더하기
날짜 : 21.01.09
유형 : 재귀
'''

def dfs(n, sum) :
    result = 0
    if n < sum :
        return 0
    if n == sum :
        return 1
    
    for i in range(1,4):
       result += dfs(n, sum+i)

    return result
    

T = int(input())
s =""
for _ in range(T):
    result = dfs(int(input()), 0)
    s += str(result)+ "\n"

print(s)

'''
재귀로 해결 
전역 변수 사용 안하고 최대한 이런식으로 한다
'''