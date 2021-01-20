
n = int(input())

s = ""

for _ in range(n):
    s += 'IO'
s += "I"

pnum = int(input())
p = input()
cnt = 0
for i in range(pnum-2*n):
    if s in p[i:i+(2*n+1)]:
        cnt += 1

print(cnt)

