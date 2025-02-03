import sys
from collections import deque

input = sys.stdin.readline

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

N, M = map(int, input().split())
data = [list(input().strip()) for _ in range(N)]
INF = 1000000
dp = [[[INF,INF] for _ in range(M)] for _ in range(N)]
dp[0][0][0] = 1

q = deque([(0,0)])

while q:
    i, j = q.popleft()
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj <M:
            if data[ni][nj] == '1':
                if dp[ni][nj][1] > dp[i][j][0] + 1:
                    dp[ni][nj][1] = dp[i][j][0] + 1
                    q.append((ni, nj))
            else:
                flag = False
                if dp[ni][nj][0] > dp[i][j][0] + 1:
                    dp[ni][nj][0] =  dp[i][j][0] + 1
                    flag = True
                if dp[ni][nj][1] > dp[i][j][1] + 1:
                    dp[ni][nj][1] = dp[i][j][1] + 1
                    flag = True
                
                if flag:
                    q.append((ni, nj))


if min(dp[N-1][M-1]) == INF:
    print(-1)
else:
    print(min(dp[N-1][M-1]))