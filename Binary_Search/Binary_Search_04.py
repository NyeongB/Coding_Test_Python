'''
출제 : 백준
난이도 : 골드 4
문제 : 세 용액
날짜 : 21.05.16
유형 : 투 포인터
'''

def find(arr,n):
    p1, p2, p3, a1, a2, a3 = 0,0,0,0,0,0
    ans = 1e9 * 5000
    for i in range(n):
        p1 = 0
        p2 = n-1
        p3 = i

        while p1 < p2:
            if p1 == p3:
                p1 += 1
            if p2 == p3:
                p2 -= 1
            if p1 == p2:
                break
            result = arr[p1]+arr[p2]+arr[p3]
            if abs(result) < ans:
                ans = abs(result)
                a1 = p1
                a2 = p2
                a3 = p3
            if result < 0:
                p1 += 1
            elif result > 0:
                p2 -= 1
            else:
                return [arr[a1],arr[a2],arr[a3]]

    return [arr[a1],arr[a2],arr[a3]]


N = int(input())

input_list = list(map(int,input().split()))

input_list.sort()

answer = find(input_list,N)

print(*sorted(answer))


'''
투 포인터 문제에서 하나 더 추가된 문제
중요한 문제다
1e9가 10억까지라 문제를 잘읽어야한다..
초기값이 10억 * 5000까진 줘야지 문제 해결 가능 
'''