'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 스킬 트리
날짜 : 21.01.11
유형 : 구현
'''
def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        index = 0
        flag = 0
        for c in skills:
            if skill.find(c) >-1:   #문자 하나씩 꺼내서 그 문제가 스킬트리에 있으면 인덱스에 맞게 스킬이 진행됐는지 확인
                if skill[index] != c :
                    flag = 1
                    break
                else :
                    index += 1
        if flag == 0:
            answer += 1
                    
    return answer

# 테스트
print(solution("CBD" , ["BACDE", "CBADF", "AECB", "BDA"]))

'''

'''