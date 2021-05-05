'''
출제 : 백준
난이도 : 실버 3
문제 : 이전 수열
날짜 : 21.05.01
유형 : 수열
'''

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def prev_permutation(lst):
    if len(lst) == 1:
        return [-1]
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] <= lst[i - 1]:
            break
    if i == 1 and lst[0] < lst[1]:
        return [-1]
    # i - 1 인덱스에 위치한애가 바뀔 것이여
    for j in range(len(lst) - 1, 0 , -1):
        if lst[j] <= lst[i - 1]:
            break
    # j 인덱스하고 바뀔 것이여
    tmp = lst[j]
    lst[j] = lst[i - 1]
    lst[i - 1] = tmp
    print(i,j)
    lst = lst[:i] + sorted(lst[i:], reverse=True)
    return lst

print(' '.join(map(str, prev_permutation(lst))))

    
'''
메모리 초과..? 
단순하게 순열로 생각했지만 
알고리즘적인 접근이 필요한것같다
이 부분이 항상 부족함..!
'''