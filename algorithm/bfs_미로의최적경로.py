from collections import deque

#입력 받기(N * M 크기의 미로)
n, m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]

def bfs(maze):
    queue = deque()
    queue.append((0,0)) #시작점
    directions = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우

    while queue: #큐가 비지 않은 상태?
        x, y = queue.popleft() #큐의 가장 최신 요소 뽑아서 x, y에 튜플값 각각 저장

        for dx, dy in directions: #direction의 튜플을 하나씩 뽑아서 dx, dy로 각각 값 저장
            nx, ny = x + dx, y + dy #최신값에 이동경로(dx,dy)값 더해서 새로운 좌표 만들어주기 

            #만약 nx, ny 크기가 미로 영역에 포함되고, 미로에서 지날 수 있는 길이라면
            #조건 순서 중요. nx 혹은 ny가 미로 크기를 벗어나면 IndexError 발생. 크기부터 유효한지 체크할 것.
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1: 
                maze[nx][ny] = maze[x][y] + 1 #직전 미로 값에 1초를 더하여 시간 체크하기
                queue.append((nx,ny)) #지난 경로를 큐에 넣기(다음 탐색 대상으로 계속 루트 확장시키기)
    
    return maze[n-1][m-1] -1 if maze[n-1][m-1] != 1 else -1 
    # maze[n-1][m-1]에는 시작점부터 목표지점까지 절린 총 칸 수가 들어있음(조건: 1,1에서 시작해여 n,m까지 이동해야 미로를 탈출할 수 있다.)
    # 이는 곧, '걸린 시간 초'를 의미(1초에 1칸 이동)
    # 첫 시작점인 maze[0][0]을 1로 계산해주기에, 초를 셀때는 -1 해줌
    # maze[n-1][m-1] == 1이면, 도착하지 못한 상태

print(bfs(maze))