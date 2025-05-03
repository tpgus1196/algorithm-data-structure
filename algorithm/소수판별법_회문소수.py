n = int(input())

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True #이게 for문 안에 있으면 num이 2보다 큰 수라도 i=2일때까지 검사하고 바로 True를 반환해버림.(ex. 9%3==0 이 되는 것을 검사도 못함)
def is_palindrome(num):
    num = str(num)
    return num == num[::-1] #문자열 뒤집기와 비교
        

cnt = 0
for _ in range(n):
    a = int(input())
    if is_prime(a) and is_palindrome(a) is True:
        cnt += 1

print(cnt)
