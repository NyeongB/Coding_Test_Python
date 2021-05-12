'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 뉴스 클러스터링
날짜 : 21.05.12
유형 : 문자열
'''

def solution(str1, str2):
    dicA = {}
    dicB={}
    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            dicA[str1[i]+str1[i+1]] = dicA.get(str1[i]+str1[i+1],0)+1
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            dicB[str2[i]+str2[i+1]] = dicB.get(str2[i]+str2[i+1],0)+1

    print(dicA,dicB)
    common = 0
    for a in dicA:
        if a in dicB:
            common += min(dicA[a], dicB[a])
    lenA = sum(dicA.values())
    lenB = sum(dicB.values())

    total = lenA + lenB - common
    if total == 0:
        return 65536

    return int(65536 * common / total)

'''
레퍼런스를 참고했다
나는 처음에 아예 집합으로만 생각해서 
확장 집합도 인덱스를 추가하는 식으로 구현했는데
해시로 접근해야 확장 집합을 만족시킬수있다
'''