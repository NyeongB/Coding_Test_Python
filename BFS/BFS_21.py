'''
출제 : 프로그래머스
난이도 : 레벨 3
문제 : 단어변환
날짜 : 21.06.14
유형 : BFS
'''
from collections import deque

def oneWordDiff(a,b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    q = deque()
    visited = set()
    
    for i in range(len(words)):
        if oneWordDiff(begin, words[i]):
            
            q.append((words[i],1))
            
    while q:
        temp,c = q.popleft()
        visited.add(temp)
        if temp == target:
            answer = c
            break
        
        for i in range(len(words)):
            if words[i] not in visited and oneWordDiff(words[i],temp):
                q.append((words[i],c+1))
        
    
    return answer

'''
예전에 자바로 풀었던 문젠데
처음부터 다시 생각해보았다
다시 bfs 응용이며 
일반적으로 푸는 4방향이 아닌 
단어가 1개 차이 나는것을 갈수있는 방향으로 놓고 푸니 한번에 풀렸다.
'''