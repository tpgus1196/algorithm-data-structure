#빠른 시간 안에 구간합 구하기 문제
#주어진 입력의 각 원소를 순차적으로 더한 결과를 구한다
#주어진 입력에서 중간 부분의 원소 합을 구할 때 많이 사용된다
import sys

n, m, k = map(int, sys.stdin.readline().split())

#원본 땅값 배열 및 누적합 배열 초기화(1-base index 사용)
arr = [[0]*3 for _ in range(3)]
pSum = [[0]*3 for _ in range(3)]
print(arr)