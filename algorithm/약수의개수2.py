# 약수의 개수를 구하는 방법2
# 약수는 항상 쌍으로 존재 1부터 √N까지 반복하면서 나누어 떨어지는 수를 탐색
# 그 수와 N을 그 수로 나눈 값을 함께 카운트. 
# 시간복잡도는 O(√N)

import math
t = int(input())

for _ in range(t):
    n = int(input())
    sqt_n = math.ceil(math.sqrt(n))
    nums = set()
    for i in range(1,sqt_n+1):
        if n % i == 0:
            nums.add(i)
            nums.add(n//i)
    if len(nums) % 2 == 0:
        print('Even')
    else:
        print('Odd')