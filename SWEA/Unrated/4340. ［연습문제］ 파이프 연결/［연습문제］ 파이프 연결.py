# 방향 정의: 오른쪽, 아래, 왼쪽, 위 (시계방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# DFS 탐색 함수 정의
# r, c: 현재 위치, d: 현재 방향, dist: 이동 거리
def dfs(r, c, d, dist):
    global ans

    # 종료 조건: 목표 지점에 도달한 경우
    if (r, c) == (tr, tc):
        ans = min(ans, dist)  # 최단 거리 갱신
        return

    # 가지치기 조건들
    if dist >= ans:  # 이미 최소 거리보다 크면 중단
        return
    if not (0 <= r < n and 0 <= c < n and arr[r][c]):  # 범위 벗어나거나 파이프 없는 칸
        return
    if visited[r][c]:  # 이미 방문한 경우 (사이클 방지)
        return
    if dp[r][c][d] < dist:  # 동일 방향에 대해 이전 방문보다 거리가 길면 의미 없음
        return

    dp[r][c][d] = dist  # 방문 정보 갱신
    visited[r][c] = True  # 방문 처리

    # 파이프 종류에 따라 연결 방향 다르게 처리
    t = arr[r][c]
    if t <= 2:  # 직선 파이프 (1: 수평, 2: 수직) -> 회전 필요 없음
        nd = d  # 현재 방향 그대로 진행
        dfs(r + dr[nd], c + dc[nd], nd, dist + 1)
    else:  # 꺾인 파이프 (3~6): 현재 방향 기준 좌/우 방향 전환 가능
        for nd in [(d + 1) % 4, (d + 3) % 4]:  # 90도 회전(오른쪽), 270도 회전(왼쪽)
            dfs(r + dr[nd], c + dc[nd], nd, dist + 1)

    visited[r][c] = False  # 백트래킹 시 방문 해제


# 테스트 케이스 개수만큼 반복
for t in range(int(input())):
    n = int(input())  # 보드 크기
    arr = [list(map(int, input().split())) for _ in range(n)]  # 파이프 정보

    ans = 10 ** 9  # 최소 거리 초기화
    visited = [[False] * n for _ in range(n)]  # 방문 체크 배열
    dp = [[[10 ** 9] * 4 for _ in range(n)] for _ in range(n)]  # 방향별 방문 거리 메모이제이션
    
    #1단계: 시작 -> 종료 방향 (오른쪽 방향으로 나가는 형태)
    tr, tc = n - 1, n  # 도착 조건: 오른쪽 바깥으로 나가는 것
    dfs(0, 0, 0, 0)  # (0,0)에서 시작, 오른쪽(0번 방향)으로 진입
	
    #2단계: 도착지에서 반대로 시작 -> 시작점으로 진입 확인 (왼쪽 방향으로 나가는 형태)
    dp = [[[10 ** 9] * 4 for _ in range(n)] for _ in range(n)]  # DP 재초기화
    tr, tc = 0, -1  # 도착 조건: 왼쪽 바깥으로 나가는 것
    dfs(n - 1, n - 1, 2, 0)  # (n-1,n-1)에서 시작, 왼쪽(2번 방향)으로 진입

    print(f"#{t + 1} {ans}")  # 최종 정답 출력
