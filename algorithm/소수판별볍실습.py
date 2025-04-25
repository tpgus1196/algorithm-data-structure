def sieve(n):
    primes = [True] * (n+1) #인덱스 0~n까지를 True로 초기화
    primes[0] = primes[1] = False #0과 1은 소수가 아님

    for i in range(2, int(n**0.5)+1): #루트n까지만 검사
        if primes[i]: #i가 아직 소수라면
            for j in range(i*i, n+1, i): #i의 배수들을 모두 지움
                primes[j] = False

    return [i for i in range(2, n+1) if primes[i]] #true인 인덱스만 소수로 반환


#예시: 100이하의 소수 출력
print(sieve(100))