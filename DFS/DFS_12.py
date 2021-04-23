'''
출제 : 백준
난이도 : 골드 5
문제 : ABCDE
날짜 : 21.04.20
유형 : DFS
'''

n, m = map(int, input().split())

arr = [([0]* n) for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1


for i in arr:
    print(''.join(map(str,i)),end="\n")

