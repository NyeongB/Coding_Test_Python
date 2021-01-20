# 21.01.20
# p.183
# 두 배열의 원소 교체

n, k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = 0

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else :
        break

print(sum(A))