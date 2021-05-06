'''
출제 : 백준
난이도 : 골드 4
문제 : 최소 스패닝 트리
날짜 : 21.05.06
유형 : 그리디
'''
parent = {}
rank = {}
input_data = []
v, e = map(int, input().split())

for _ in range(e):
    input_data.append(tuple(map(int, input().split())))

input_data.sort(key=lambda x:x[2])

def make_set(v):
    for i in range(1, v+1):
        parent[i] = i
        rank[i] = 0
    
def find(v):

    if v != parent[v]:
        parent[v] = find(parent[v])

    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else :
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

ans = 0
make_set(v)

for i in input_data:
    x, y, r = i

    if find(x) != find(y):
        union(x,y)
        ans += r

print(ans)

'''
방식은 정확히 이해했다.
파인드로 서로 같은 트리에 있는지 사이클이 아닌지를 파악하고
유니온으로 같은 트리로 묶고
비용이 제일 낮은거를 먼저 넣으면서 최소 신장 트리를 만든다
당분간은 외워서 구현하도록 한다
'''