#무방향 그래프에서 연결 요소 개수 찾기
#1-2-3 연결, 4-5 연결 시 컴포넌트 2개
#목표: 서로 떨어진 컴포넌트가 몇 개인지 알아내기
#할일: 모든 정점 하나씩 훑기 > 방문 안한 정점이 있다면 DFS로 연결된 노드 탐색 > DFS로 탐색이 끝났다는 건 한 컴포넌트를 다 본 것 > cnt += 1

def dfs(n):
    #현재 노드와 연결된 노드를 탐색
    for i in v[n]: 
        if not visited[i]:
            visited[i] = True #방문 처리. 방문 여부 먼저기록하는 이유는 DFS재귀 시 무한루프 방지
            dfs(i) #재귀 DFS 호출

#정점 수 N, 간선 수 M 입력
n, m = map(int, input().split())

visited = [False] * 201 #방문 여부 배열(1~N까지 사용)
cnt = 0 #컴포넌트 개수 세는 변수
v = [[] for _ in range(201)] #인접 리스트로 그래프 초기화

#간선 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a) #무방향이므로 양쪽 다 연결

#모든 정점에 대해 DFS 수행
for i in range(1, n+1):
    if not visited[i]: #방문하지 않은 정점이면 새 컴포넌트 시작
        visited[i] = True 
        dfs(i) #DFS로 해당 컴포넌트 전체 탐색
        cnt += 1 #컴포넌트 하나 발견

print(cnt) #컴포넌트 개수 출력