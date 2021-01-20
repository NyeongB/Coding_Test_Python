'''
출제 : 백준
난이도 : 실버 5
문제 : 그룹 단어 체커
날짜 : 21.01.20
유형 : 문자열
'''
n = int(input())
cnt = 0
for _ in range(n):
    
    alpha = [0] * 26
    flag = 0
    s = input()
    
    for i, v in enumerate(s):
        index = ord(v) - 97
        if alpha[index] != 0:
            if s[i-1] != s[i]:
                flag = 1
                break
        alpha[index] += 1
    
    if not flag :
         cnt += 1

print(cnt)

'''
아스키코드 변환 ord() 사용
'''