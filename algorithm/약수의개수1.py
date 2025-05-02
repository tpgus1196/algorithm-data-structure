
#t개의 숫자를 입력받았을 때 해당 숫자들의 약수가 홀수개인지, 짝수개인지 판별
#O(n)의 시간복잡도(첫번째 for문은 테스트케이스의 수만큼 반복되기 때문에, 전체 시간복잡도에 큰 영향을 주지 않는다)
#엄밀히 말하면 O(t*n)의 시간복잡도. 하지만 상수는 무시하고, 가장 큰 영향을 주는 항만 고려하기때문에 t는 버리고 표기.

t = int(input())
cnt = 0

for _ in range(t):
    nums = [1]
    n = int(input())
    for i in range(2,n+1):
        if n%i == 0:
            nums.append(i)

    if len(nums) % 2 == 0:
        print('Even')
    else:
        print('Odd')