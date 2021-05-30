'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 스킬트리
날짜 : 21.05.30
유형 : 구현
'''
def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    
    for i in skill_trees:
        flag = True
        temp = list(i)
        index = 0
        for j in temp:
            if j in skill_list:
                if j != skill_list[index]:
                    flag = False
                    break
                else:
                    index += 1
        
        if flag:
            answer += 1
                
    
    return answer

'''
'''