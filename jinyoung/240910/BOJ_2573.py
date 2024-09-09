import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 4방향 이동 정의
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# BFS로 섬의 개수 체크
def check():
    visited = [[0] * M for _ in range(N)]
    que = deque()
    count = 0

    for i in range(N):
        for j in range(M):
            if my_map[i][j] > 0 and not visited[i][j]:
                count += 1
                que.append((i, j))
                visited[i][j] = 1

                while que:
                    x, y = que.popleft()

                    for di, dj in move:
                        ni = x + di
                        nj = y + dj
                        if 0 <= ni < N and 0 <= nj < M and my_map[ni][nj] > 0 and not visited[ni][nj]:
                            que.append((ni, nj))
                            visited[ni][nj] = 1

    return count

# 입력 받기
N, M = map(int, input().split())
my_map = [[*map(int, input().split())] for _ in range(N)]

year = 0

# 섬이 있는 좌표를 따로 큐에 저장해서 관리
while True:
    year += 1
    melt_list = []  # 녹을 좌표와 바다에 닿은 면적 정보 저장

    # 주변 바다 면적 계산
    for i in range(N):
        for j in range(M):
            if my_map[i][j] > 0:
                count = 0
                for di, dj in move:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M and my_map[ni][nj] == 0:  # 바다일 때
                        count += 1
                if count > 0:
                    melt_list.append((i, j, count))

    # 섬 녹이기
    for i, j, cnt in melt_list:
        my_map[i][j] -= cnt
        if my_map[i][j] < 0:
            my_map[i][j] = 0

    # 섬 개수 체크
    island_count = check()
    if island_count == 0:  # 섬이 모두 녹았다면
        print(0)
        break
    elif island_count >= 2:  # 섬이 2개 이상으로 나뉘었다면
        print(year)
        break
