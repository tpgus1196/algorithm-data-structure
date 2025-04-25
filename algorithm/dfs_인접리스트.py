#인접 리스트 방식 그래프 정의
graph = [
    [], #0번 노드는 사용하지 않음
    [2, 3], #1번 노드는 2, 3번 노드로 연결됨
    [], #2번 노드는 연결 없음
    [], #3번 노드도 연결 없음
    [] #4번 노드는 연결 없음(예비공간)
]

visited = [False] * 5 #방문 여부 저장 배열
access_count = 0 #실제로 접근한 횟수를 세는 변수

def dfs_list(now):
    global access_count
    visited[now] = True #현재노드 방문표시
    print(now, end = ' ') #현재노드 출력

    for next_node in graph[now]: #연결된 노드만 순회
        access_count += 1 #연결된 노드에 접근하므로 접근 횟수 증가
        if not visited[next_node]: #아직 방문하지 않은 노드라면
            dfs_list(next_node) #dfs 재귀 호출

dfs_list(1) #1번 노드에서 dfs 시작
print('\n접근 횟수 (리스트):', access_count)