import heapq

def heap_sort(arr):
    # 1. 힙으로 변환 (최소 힙)
    heapq.heapify(arr)

    # 2. 하나씩 꺼내서 정렬 리스트에 추가
    sorted_list = []
    while arr:
        sorted_list.append(heapq.heappop(arr))  # 최솟값 꺼냄

    return sorted_list

#예제 리스트
data = [7, 2, 5, 1, 9, 3]

#힙 정렬 실행
result = heap_sort(data.copy()) # 원본 보호 위해 copy()

#결과 출력
print('정렬 결과 (오름차순):', result)