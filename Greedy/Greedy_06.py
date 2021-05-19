'''
출제 : 프로그래머스
난이도 : 레벨 3
문제 : 섬 연결하기
날짜 : 21.05.19
유형 : 그리디, 크루스칼
'''
parent = {}
rank = {}

def make_set(n):
    for i in range(0,n):
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
        
    


def solution(n, costs):
    answer = 0
    
    make_set(n)
    costs.sort(key=lambda x:x[2])
    
    for u,v,r in costs:
        if find(u) != find(v):
            union(u,v)
            answer += r
            
    
    return answer