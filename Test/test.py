

n, e = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(e)]

arr.sort(key=lambda x:x[2])

parent = {}
rank = {}
ans = 0

def make_set(n):
    for i in range(1,n+1):
        parent[i] = i
        rank[i] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u,v):
    root1 = find(u)
    root2 = find(v)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

make_set(n)

for u,v,r in arr:
    if find(u) != find(v):
        union(u,v)
        ans += r


print(ans)