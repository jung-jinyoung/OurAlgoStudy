def solution(triangle):
    N = len(triangle)
    dp = [[0]*i for i in range(1, N+1)]
    
    
    for j in range(N):
        dp[N-1][j] = triangle[N-1][j]
    
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j] ,dp[i+1][j+1])
    return dp[0][0]