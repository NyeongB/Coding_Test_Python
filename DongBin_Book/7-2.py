'''
문제 : 이진 탐색 재귀 예제
날짜 : 21.04.25
유형 : binary search
'''

def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        
    return None


arr = [0,1,2,3,4,5,6,7,8,9,10]
target = 11

result = binary_search(arr,target,0,len(arr)-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)