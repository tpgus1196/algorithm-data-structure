n = int(input())

#배열
primes=[True]*(n+1) #인덱스 0~N까지 True로 초기화
primes[0] = primes[1] = False #0과 1은 소수가 아님(주의)

#인덱스로 소수 판별하기
#제곱근 이하의 수들을 구하여 배수를 제거해주기
for i in range(2, int(n**0.5)+1):
    for j in range(i*i,n+1,i): #i의 배수부터 n+1까지, i 간격으로 = i 배수
        primes[j] = False

#[print(i,end=' ') for i in range(1,n+1) if primes[i]]
result = []
for i in range(2,n+1): 
    if primes[i]:
        result.append(i)
print(len(result))