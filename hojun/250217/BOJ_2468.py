# 안전영역

from collections import deque

di = [0,1,0,-1]
dj = [1,0,-1,0]
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

max_h = max(map(max, data))

answer = 1

for h in range(1, max_h):
    area = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and data[i][j] > h:
                area += 1
                if data[i][j] > h:
                    q = deque([(i, j)])
                    visited[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx = x + di[k]
                            ny = y + dj[k]
                            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                                if data[nx][ny] > h:
                                    visited[nx][ny] = True
                                    q.append((nx, ny))
                                else:
                                    visited[nx][ny] = True
            elif not visited[i][j] and data[i][j] <= h:
                visited[i][j] = True
    answer = max(answer, area)

print(answer)