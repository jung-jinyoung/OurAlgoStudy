N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(1+N)]            # [가로,세로,대각], 행에만 한 줄 버퍼
dp[1][1][0] = 1                                                 # 파이프 초기 상태 우측 끝을 1로 설정
for i in range(1,1+N):                                          # 행은 위에 한 줄의 버퍼가 있으므로
    for j in range(2,N):                                        # 열은 0,1이 절대 불가이므로 2부터!
        if not arr[i-1][j]:                                     # 두고자 하는 칸은 벽이 아니어야 한다
            dp[i][j][0] += (dp[i][j-1][0] + dp[i][j-1][2])      # 가로는 이전의 가로와 대각선의 합
            dp[i][j][1] += (dp[i-1][j][1] + dp[i-1][j][2])      # 세로는 이전의 세로와 대각선의 합
            if arr[i-2][j]==0 and arr[i-1][j-1]==0:             # 왼쪽과 윗부분에도 벽이 있으면 안 됨
                dp[i][j][2]+=sum(dp[i-1][j-1])                  # 대각선은 이전 상태 상관없음
print(sum(dp[N][N-1]))
