#큰 문제들을 작은 문제로 분할 + 작은 문제들의 답으로 큰 문제의 답을 구함
def fibo(N):
    if N < 2: #N이 2이하일 때, 1 반환 = 기저 사례
        return 1
    return fibo(N-1) + fibo(N-2)