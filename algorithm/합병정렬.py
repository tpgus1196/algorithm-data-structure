def merge_sort(arr, depth =0):
    print(f'[정렬 시작] 배열: {arr}') #각 정렬 시작 시 출력

    if len(arr) <= 1:
        print(f'반환(정렬 완료): {arr}\n') #반환 시 구분 출력
        return arr
    
    mid = len(arr) //2
    left = merge_sort(arr[:mid], depth + 1) #왼쪽 재귀
    right = merge_sort(arr[mid:], depth + 1) #오른쪽 재귀

    print(f'병합 시작: {left} + {right}') #병합 시작 표시
    merged = merge(left, right)
    print(f'병합 완료: {merged}') #병합 완료 표시
    print('-'*40) #구분선으로 단계 구분
    return merged

def merge(left, right):
    result = []
    i = j = 0

    #병합 처리: 두 리스트에서 작은 값부터 꺼냄
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    #남은 요소 추가
    result.extend(left[i:]), result.extend(right[j:])
    return result

#실행
arr = [5, 3, 1, 4, 2]
print('초기 배열:', arr), print('-'*40)
sorted_arr = merge_sort(arr)
print('-'*40),print('최종 정렬 결과:', sorted_arr)