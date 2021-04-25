'''
문제 : 부품 찾기
날짜 : 21.04.25
유형 : binary search
'''
def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return 'yes'
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    
    return 'no'

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

result = []

for i in x:
    result.append(binary_search(arr,i,0,n))

for i in result:
    print(i,end=' ')



'''
5
8 3 7 9 2
3
5 7 9
->
no yes yes
'''