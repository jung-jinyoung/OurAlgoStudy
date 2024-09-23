def solution(m, n, puddles):
    mod = 1000000007
    dp = [[0]*(m) for _ in range(n)]
    
    for i in range(n):
        if [1,i+1] in puddles:
            break
        dp[i][0]=1
    for j in range(m):
        if [1+j,1] in puddles:
            break
        dp[0][j]=1
    for i in range(1,n):
        for j in range(1,m):
            if [j+1,i+1] not in puddles:
                dp[i][j]=(dp[i][j-1]+dp[i-1][j])%mod
    # print(dp)
    return dp[n-1][m-1]