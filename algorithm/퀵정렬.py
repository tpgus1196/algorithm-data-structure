compare_count = 0 #총 비교 횟수를 저장하는 변수
pivot_history = [] #피벗 값들이 선택된 순서를 저장하는 리스트

def quick_sort(arr):
    global compare_count, pivot_history #전역 변수 사용 선언
    print(f'정렬할 배열: {arr}\n')

    if len(arr) <= 1:
        print(f'반환: {arr}') #배열 길이가 0 또는 1이면 이미 정렬된 상태
        return arr #그대로 반환
    
    pivot = arr[0] #피벗: 배열의 첫 번째 요소 선택
    pivot_history.append(pivot) #선택된피벗을 기록 리스트에 저장

    left = [] #피벗보다 작은 값을 담을 리스트
    right = [] #피벗보다 크거나 같은 값을 담을 리스트

    for x in arr[1:]: #피벗을 제외한 나머지 값들 반복
        compare_count +=1 #비교 횟수 1 증가
        if x < pivot: #피벗보다 작으면
            left.append(x) #left쪽에 추가
        else:
            right.append(x) #크거나 같으면 right 쪽에 추가

    print(f'피벗: {pivot}') #현재 선택된 피벗 출력
    print(f'작은 값들: {left}'), print(f'큰 값들: {right}')
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right) #왼쪽/오른쪽 부분 재귀 정렬

    result = sorted_left + [pivot] + sorted_right #병합:왼쪽+피벗+오른쪽
    print(f'병합 결과: {result}')
    return result

#실행 부분
arr = [5, 3, 1, 4, 2]
print('초기 배열:', arr) #시작 메시지 출력


sorted_arr = quick_sort(arr) #퀵 정렬 실행 및 결과 저장
print('\n최종 정렬 결과:', sorted_arr) #최종 정렬 결과
print(f'총 비교 횟수:{compare_count}') #총 비교 횟수
print(f'피벗 선택 순서: {pivot_history}') #피벗 선택 순서
