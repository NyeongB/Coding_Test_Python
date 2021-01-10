'''
출제 : 백준
난이도 : 골드5
문제 : 암호 만들기
날짜 : 21.01.10
유형 : 재귀
'''

L, C = map(int, input().split())
alpha = sorted(input().split()) # alpha = list(map(str, input().split())) -> alpha.sort()
out = []
result = []
all_out = []

# 조합
def combi(index,depth,L,C) :
    if depth == L :
        result.append("".join(map(str,out)))
        return

    for i in range(index, C) :
        out.append(alpha[i])
        combi(i+1, depth+1, L, C)
        out.pop()

# a e i o u 가 포함되어있는지 확인
def check(result) :
    for string in result:
        count_1 = 0
        count_2 = 0
        for char in string :
            if char in "aeiou":
                count_1 += 1
            else :
                count_2 += 1
        if count_1 > 0 and count_2 > 1:
            all_out.append(string)
    return

combi(0,0,L,C)
check(result)
for string in all_out:
    print(string)

'''
파이썬에는 딕셔너리라는 자료형이 존재
hash()랑 함께 쓰이는것같음
하지만 기본적인 해시 구조로 풀어봄
'''