def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j] 
    return arr            

data = [5, 3, 1, 4, 2]
print('정렬 전:', data)
sorted_data = bubble_sort(data.copy())
print('\n정렬 후:', sorted_data)