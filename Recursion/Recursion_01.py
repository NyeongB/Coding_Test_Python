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
파이썬에는 딕셔너리라는 자료형이 존재
hash()랑 함께 쓰이는것같음
하지만 기본적인 해시 구조로 풀어봄
'''