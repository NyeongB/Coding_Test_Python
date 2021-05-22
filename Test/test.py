parent = {}
rank = {}

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

n, m = map(int, input().split())

arr = [list(map(int,input().split()))for _ in range(m)]
make_set(n)
for a,b in arr:
    if find(a) != find(b):
        union(a,b)

answer = set()

for k,v in parent.items():
    answer.add(v)

print(len(answer))