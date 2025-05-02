#O(√N) 시간복잡도
import math
n, m = map(int, input().split())

#n과 m의 약수 구하기
def gcd(n):
    nums = set()
    sqt_n = math.ceil(math.sqrt(n))
    for i in range(1,sqt_n+1):
        if n % i == 0:
            nums.add(i)
            nums.add(n//i)
    return nums

#교집합
intersect = list(gcd(n).intersection(gcd(m))) #gcd(n) & gcd(m)

#합집합(참고)
#union = list(gcd(n).union(gcd(m))) #gcd(n) | gcd(m)

#최대공약수
a = max(intersect)

#최소공배수(두 수의 곱을 최대공약수로 나눈 값)
b = (n*m) // a

print(a, b)
