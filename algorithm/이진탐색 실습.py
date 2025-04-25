def binary_search(arr, target):
    left = 0 #인덱스 시작
    right = len(arr) -1 #인덱스 끝
    count = 0 #몇 번 탐색했는지 카운트

    while left <= right:
        count += 1 #반복될 때마다 +1
        mid = (left+right) // 2
        print(f'[{count}회차] 중간 인덱스 = {mid}, 값 = {arr[mid]}')

        if arr[mid] == target:
            print(f'{count}번만에 타겟 {target}을 찾았습니다!')
            return mid
        elif arr[mid] < target:
            left = mid + 1 #오른쪽 탐색
        else:
            right = mid -1 #왼쪽 탐색
    
    print(f'{count}번 탐색했지만 타겟 {target}을 찾지 못했습니다.')
    return -1

#테스트 배열과 타겟
arr = [1, 3, 5, 7, 9, 11, 13]
target = 11

#tlfgod
result = binary_search(arr, target)
print("찾은 인덱스:", result)