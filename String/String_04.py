'''
출제 : 백준
난이도 : 실버 2
문제 : IOIOI
날짜 : 21.01.20
유형 : 문자열
'''
N = int(input())
M = int(input())
S = input()

answer = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)

'''
처음엔 2n+1 개의 IOI.. 를만들어 
S를 슬라이싱해서 in으로 True 반환해서 answer += 1을 하였는데 바로 시관초과..
해서 이방법을 보았는데 정말 완벽한 풀이법같다...
'''