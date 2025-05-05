# 크기가 N인 배열 a
# M의 값이 주어질 때, a배열에서 서로 연속된 m개의 값을 골라 합을 구한다
# 합의 최댓값을 구하는 프로그램
n, m = map(int, input().split())

a = list(map(int, input().split()))

curr_sum = sum(a[:m]) #0번부터 m-1번까지 더하기
max_sum = curr_sum

#연속된 수 m개의 합
for i in range(m,n):
    #i~i+m까지 합
    #한칸 이동시킨만큼 빼주기
    curr_sum += a[i] - a[i-m]
    max_sum = max(max_sum,curr_sum)
    #직전합, 현재합 중 최대
print(max_sum)