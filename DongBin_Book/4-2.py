'''
문제 : 상하좌우
날짜 : 21.03.22
유형 : 시각
'''

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count = count + 1

print(count)

'''
3중 for문으로 해결해야하는 문제
모든 수를 문자열로 더한후 '3' in str 한거는 정말 편한듯
'''