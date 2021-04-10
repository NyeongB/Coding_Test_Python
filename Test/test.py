orders = ['choi pizza hamberger steak', 'lee noodle hamberger pasta', 'park kimchi sandwich pizza',
'choi hamberger pasta steak']

def solution(orders):
    answer = []
    hm = {}
    for i in orders:
        a = i.split()
        hm[a[0]] = set()
        for j in range(1,len(a)):
            hm[a[0]].add(a[j])

    m = []

    for k,v in hm.items():
        m.append(len(v))

    for k,v in hm.items():
        if max(m) == len(v):
            answer.append(k)    
    a.sort()
    return answer


print(solution(orders))