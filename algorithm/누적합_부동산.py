#빠른 시간 안에 구간합 구하기 문제
#주어진 입력의 각 원소를 순차적으로 더한 결과를 구한다
#주어진 입력에서 중간 부분의 원소 합을 구할 때 많이 사용된다
import sys

n, m, k = map(int, sys.stdin.readline().split())

#원본 땅값 배열 및 누적합 배열 초기화(1-base index 사용)
arr = [[0]*1001 for _ in range(1001)]
pSum = [[0]*1001 for _ in range(1001)]

#입력받은 땅값 배열을 arr에 저장하고 동시에 누적합 배열 pSum 계산
for i in range(1, n+1): #행
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, m+1): #열
        arr[i][j] = row[j-1]
        #누적합 공식: pSum[i][j] = 위+왼 - 겹치는부분 + 현재값
        pSum[i][j] = (
            pSum[i-1][j] +
            pSum[i][j-1] -
            pSum[i-1][j-1]+
            arr[i][j]
        )

#k개의 질의 처리: (a,b) ~(c,d) 사각형 구간 합 출력
for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    result = (
        pSum[c][d] -
        pSum[c][b-1] -
        pSum[a-1][d] +
        pSum[a-1][b-1]
    )
    print(result)