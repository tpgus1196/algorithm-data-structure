def fibonacci_iter(n):
    a, b = 0, 1 #초기 피보나치 값 설정: F(0) = 0, F(1) = 1
    for _ in range(n): #n번 반복
        a, b = b, a+b #a에 F(N), b에 F(N+1)을 저장
    return a #N번째 피보나치 수 반환
print(fibonacci_iter(40))