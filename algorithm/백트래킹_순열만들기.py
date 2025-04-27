# 백트래킹 - 문제를 푸는 전략
# 해당 전략을 구현할 때 DFS(깊이 우선 탐색)을 활용한다
n, m = list(map, int(input().split()))

s = []

def dfs():
    #길이가 m인 조합이 완성되면 출력하고 종료
    if len(s) == m:
        print(' '.join(map(str,s)))
        #리스트 s를 문자열로 변환 후 공백으로 출력
        return
    
    for i in range(1, n+1): #1~n까지 숫자를 반복하며 선택 시도
        if i not in s: #중복 방지를 위해 이미 선택된 숫자는 제외 
            s.append(i) #숫자 i를 선택(현재 경로에 추가)
            dfs() #재귀 호출하여 다음 숫자 선택
            s.pop() #백트래킹:마지막에 선택한 숫자 제거(되돌리기)

dfs() #dfs탐색 시작