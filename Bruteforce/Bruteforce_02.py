'''
출제 : 백준
난이도 : 브론즈 2
문제 : 일곱 난쟁이
날짜 : 21.04.11
유형 : 브루트포스
'''
from itertools import combinations

arr = []

for _ in range(9):
    arr.append(int(input()))

a = list( combinations(arr,7) )

for i in a:
    if sum(i) == 100:
        answer = i
        break

l = list(answer)
l.sort()

for i in l :
    print(i)

'''
입력값이 작아서 조합으로 해봤다
원래는 2중 for문으로 했던것같다
'''