'''
출제 : 백준
난이도 : 골드 4
문제 : 네트워크 연결
날짜 : 21.05.19
유형 : 그리디, 크루스칼
'''

parent = dict()
rank = dict()

n = int(input())
m = int(input())

coms = [tuple(map(int,input().split())) for _ in range(m)]

coms.sort(key=lambda x:x[2])

ans = 0

def make_set(n):
    for i in range(1,n+1):
        parent[i] = i
        rank[i] = 0

def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = parent[u]
    root2 = parent[v]

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
make_set(n)
for a,b,r in coms:
    if find(a) != find(b):
        union(a,b)
        ans += r

print(ans)            
