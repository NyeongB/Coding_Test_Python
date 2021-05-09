'''
출제 : 백준
난이도 : 실버 5
문제 : 달팽이
날짜 : 21.05.09
유형 : 별찍기
'''

n = int(input())
target = int(input())

arr = [[0]*n for _ in range(n)]
row = -1
col = 0
total = n * n
flag = 1
answer =''
while n > 0:
    
    for _ in range(n):
        row += flag
        arr[row][col] = total
        if total == target:
            answer = str(row+1)+" "+str(col+1)
        total -= 1

    n = n -1

    for _ in range(n):
        col += flag
        arr[row][col] = total
        if total == target:
            answer = str(row+1)+" "+str(col+1)
        total -= 1

    flag *= -1

for i in arr:
    print(' '.join(map(str,i)),end='\n')
print(answer)