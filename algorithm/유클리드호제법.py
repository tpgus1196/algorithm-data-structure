def gcd(a, b):
    #유클리드 호제법으로 최대공약수 (GCD) 계산
    while b != 0:
        temp = a #현재 a를 저장
        a = b #b를 a로 교체
        b = temp % b #b가 0이되면 a가 최대공약수
    return a