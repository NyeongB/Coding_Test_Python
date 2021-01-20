# 21.01.20
# p.178
# 위에서 아래로

n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
