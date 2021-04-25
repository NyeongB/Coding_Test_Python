'''
문제 : 이진 탐색 재귀 예제
날짜 : 21.04.25
유형 : binary search
'''


def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    
    if arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)


arr = [0,1,2,3,4,5,6,7,8,9,10]
target = 0

result = binary_search(arr,target,0,len(arr)-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)